import cv2

img_a = cv2.imread('/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/a.png')
img_b = cv2.imread('/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/lakeb.png')

# crop center 400x400 around the person
h, w = img_a.shape[:2]
crop_a = img_a[h//2-200:h//2+200, w//2-200:w//2+200]
cv2.imwrite('.tmp/crop_a.png', crop_a)

h, w = img_b.shape[:2]
crop_b = img_b[h//2-200:h//2+200, w//2-200:w//2+200]
cv2.imwrite('.tmp/crop_b.png', crop_b)

print("Cropped images saved to .tmp/")
