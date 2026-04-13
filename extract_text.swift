import Foundation
import Vision
import Cocoa

guard CommandLine.arguments.count > 1 else {
    print("Please provide an image path.")
    exit(1)
}

let imagePath = CommandLine.arguments[1]
let url = URL(fileURLWithPath: imagePath)

guard let image = NSImage(contentsOf: url),
      let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    print("Could not load image.")
    exit(1)
}

let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
let request = VNRecognizeTextRequest { request, error in
    guard let observations = request.results as? [VNRecognizedTextObservation], error == nil else {
        print("Error recognizing text: \(String(describing: error))")
        return
    }
    
    let text = observations.compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
    print(text)
}

request.recognitionLevel = .accurate
request.usesLanguageCorrection = true

do {
    try requestHandler.perform([request])
} catch {
    print("Failed to perform text recognition: \(error)")
}
