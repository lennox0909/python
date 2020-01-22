import cv2
import numpy as np

v = cv2.VideoCapture("homework3.mp4")
'''如果輸入數字，則讀取當前電腦連結的攝影機。如果輸入檔案路徑，則讀取指定路徑的影片檔案。'''

while True:
    t, vc = v.read()
    # print("是否載入影片？", t)
    # new1 = np.full(vc.shape, 255, np.uint8)
    # new2 = np.full(vc.shape, 255, np.uint8)
    if t == True:
        # • cv2.MORPH_OPEN:先執行侵蝕後執行膨脹 (亮的會被清掉)
        # • cv2.MORPH_CLOSE:先執行膨脹後執行侵蝕 (暗的會被清掉)
        # • cv2.MORPH_GRADIENT:執行膨脹與侵蝕產生的變化差
        # vc2 = cv2.morphologyEx(vc, cv2.MORPH_GRADIENT, np.ones((15, 15)))
        # t, new1[:, :, 0] = cv2.threshold(vc[:, :, 0], 127, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        # t, new1[:, :, 1] = cv2.threshold(vc[:, :, 1], 127, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        # t, new1[:, :, 2] = cv2.threshold(vc[:, :, 2], 127, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
        # vcgray = cv2.cvtColor(vc2, cv2.COLOR_BGR2GRAY)
        vc2 = cv2.Canny(vc, 200, 50)
        cv2.imshow("Pretreat", vc2)
        a, b = cv2.findContours(vc2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        xL = []
        yL = []
        wL = []
        hL = []
        for d in a:
            x, y, w, h = cv2.boundingRect(d)
            xL.append(x)
            yL.append(y)
            wL.append(w)
            hL.append(h)
        try:
            xx = min(xL)
            yy = min(yL)
            ww = max(wL)
            hh = max(hL)
        except ValueError:
            continue
        cv2.rectangle(vc, (xx, yy), (xx + ww, yy + hh), (0, 0, 255), 2)
        # cv2.rectangle(vc, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("Video", vc)
        if cv2.waitKey(40) == 13:
            break
    else:
        break

cv2.destroyAllWindows()

##########
