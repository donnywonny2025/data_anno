import cv2
import numpy as np

img_a = cv2.imread('/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/chandeliera.png')
img_b = cv2.imread('/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/chandelierb.png')

# Let's crop to the table settings in both to show the detail difference
crop_a = img_a[700:1000, 200:800]
crop_b = img_b[700:1000, 200:800]

cv2.imwrite('.tmp/crop_a.png', crop_a)
cv2.imwrite('.tmp/crop_b.png', crop_b)
