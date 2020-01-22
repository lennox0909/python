import cv2
# import numpy as np

img = cv2.imread("0830_google.png", 1)
cv2.imshow("Image", img)
print("img shape:", img.shape)  # h, w, channel
print("img shape:", img.shape[:2])
rangeN = 100
img_filter = cv2.inRange(img,
                         (max(255 - rangeN, 0), max(255 - rangeN, 0), max(255 - rangeN, 0)),
                         (min(255 + rangeN, 255), min(255 + rangeN, 255), min(255 + rangeN, 255)))
img_filter2 = cv2.bitwise_not(img_filter)
cv2.imshow("img_filter2", img_filter2)

cv2.waitKey(0)
cv2.destroyAllWindows()
