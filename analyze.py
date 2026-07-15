import cv2
import numpy as np
from PIL import Image, ImageChops, ImageEnhance

def get_ela(img_path, quality=90):
    img = Image.open(img_path).convert('RGB')
    tmp_path = img_path + ".tmp.jpg"
    img.save(tmp_path, 'JPEG', quality=quality)
    tmp_img = Image.open(tmp_path)
    ela = ImageChops.difference(img, tmp_img)
    extrema = ela.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    ela = ImageEnhance.Brightness(ela).enhance(scale)
    return ela

img_a_path = '/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/a.png'
img_b_path = '/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/lakeb.png'

ela_a = get_ela(img_a_path)
ela_a.save('.tmp/ela_a.jpg')
ela_b = get_ela(img_b_path)
ela_b.save('.tmp/ela_b.jpg')

# Let's also do a strong contrast enhancement on the center crops
img_a = cv2.imread(img_a_path)
h, w = img_a.shape[:2]
crop_a = img_a[h//2-200:h//2+200, w//2-200:w//2+200]
crop_a_enh = cv2.convertScaleAbs(crop_a, alpha=2.5, beta=50)
cv2.imwrite('.tmp/enh_a.png', crop_a_enh)

img_b = cv2.imread(img_b_path)
h, w = img_b.shape[:2]
crop_b = img_b[h//2-200:h//2+200, w//2-200:w//2+200]
crop_b_enh = cv2.convertScaleAbs(crop_b, alpha=2.5, beta=50)
cv2.imwrite('.tmp/enh_b.png', crop_b_enh)

# And check for metadata
with Image.open(img_a_path) as im:
    print(f"Image A format: {im.format}, mode: {im.mode}, info: {im.info}")
with Image.open(img_b_path) as im:
    print(f"Image B format: {im.format}, mode: {im.mode}, info: {im.info}")

print("Analysis images saved to .tmp/")
