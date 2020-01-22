import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

v = cv2.VideoCapture("sample.mp4")
'''如果輸入數字，則讀取當前電腦連結的攝影機。如果輸入檔案路徑，則讀取指定路徑的影片檔案。'''

while True:
    t, vc = v.read()
    # print("是否載入影片？", t)
    if t == True:
        cv2.imshow("Video", vc)
        if cv2.waitKey(42) == 13:
            break
    else:
        break

cv2.destroyAllWindows()