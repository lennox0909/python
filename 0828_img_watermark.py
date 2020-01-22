import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

m = cv2.imread("2018_0101.png", 1)
# print(m)
print(m.shape)
print("維度：", len(m.shape))
h = m.shape[0]
w = m.shape[1]
c = m.shape[2]
print("高：", h, "寬：", w, "色彩空間通道數：", c)

m2 = cv2.cvtColor(m, cv2.COLOR_BGR2HSV)
m3 = cv2.cvtColor(m, cv2.COLOR_BGR2RGB)

m4 = np.full((220, 550, 3), (200, 150, 50), np.uint8)
cv2.line(m4, (10,10), (540,210), (100,100,100), 5)
cv2.rectangle(m4, (10,10), (540,210), (0,190,0), 3)
cv2.circle(m4, (275,110), 100, (0,0,190), 2)
# cv2.imwrite("2018_0102.jpg", m, [cv2.IMWRITE_JPEG_QUALITY, 100])
# cv2.imwrite("2018_0102.png", m2)

# cv2.imshow("Image M", m)
# cv2.imshow("Image M2", m2)
# cv2.imshow("Image M3", m3)
m4 = Image.fromarray(m4)
f = ImageFont.truetype("Arial_Unicode.ttf", 50)
ImageDraw.Draw(m4).text((100,100), "浮水印", (255,255,255), f)
m4=np.array(m4)

cv2.imshow("Image M4", m4)
cv2.waitKey(0)
cv2.destroyAllWindows()
