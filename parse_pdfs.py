import pypdf
import os

files = [
    '/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/knowledgebase/Achilles/AEF',
    '/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/knowledgebase/Achilles/SideBySide.pdf'
]

for file in files:
    try:
        reader = pypdf.PdfReader(file)
        text = '\n'.join(page.extract_text() for page in reader.pages)
        basename = os.path.basename(file)
        with open(f'/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/.tmp/{basename}.txt', 'w') as f:
            f.write(text)
        print(f"Extracted {file} to .tmp/{basename}.txt")
    except Exception as e:
        print(f"Error extracting {file}: {e}")
