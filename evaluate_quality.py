import cv2
import numpy as np

img_a = cv2.imread('/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/chandeliera.png')
img_b = cv2.imread('/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/chandelierb.png')

def get_blur_score(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

blur_a = get_blur_score(img_a)
blur_b = get_blur_score(img_b)

def get_color_stats(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return {
        'avg_saturation': np.mean(hsv[:,:,1]),
        'avg_value': np.mean(hsv[:,:,2])
    }

color_a = get_color_stats(img_a)
color_b = get_color_stats(img_b)

print(f"Image A - Sharpness (Laplacian Variance): {blur_a:.2f}")
print(f"Image A - Avg Saturation: {color_a['avg_saturation']:.2f}")
print(f"Image B - Sharpness (Laplacian Variance): {blur_b:.2f}")
print(f"Image B - Avg Saturation: {color_b['avg_saturation']:.2f}")

