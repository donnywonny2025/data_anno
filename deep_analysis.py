import cv2

img_b = cv2.imread('/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/chandelierb.png')

# Crop 1: The "Complex" Chandelier Crystals (Top Center)
# This will show they are just blurry, undefined blobs of light, not sharp glass
crop_crystals = img_b[50:300, 300:600]

# Crop 2: The "Complex" Flowers (Center Table)
# This will show the petals look like melted plastic, not sharp organic matter
crop_flowers = img_b[550:750, 400:800]

# Crop 3: The Crystal Goblet (Center Right)
# Shows the etched glass pattern is completely warped and lacks sharp edges
crop_glass = img_b[600:850, 650:850]

cv2.imwrite('.tmp/crop_b_crystals.png', crop_crystals)
cv2.imwrite('.tmp/crop_b_flowers.png', crop_flowers)
cv2.imwrite('.tmp/crop_b_glass.png', crop_glass)
