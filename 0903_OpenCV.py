import cv2
import numpy as np

m1 = cv2.imread("Terminalia.jpg", 1)  # 0 => gray
cv2.imshow("Image M1", m1)
# 變數一, 變數二=cv2.threshold(圖像變數, 門檻值, 最大值, 方法)
t, m2 = cv2.threshold(m1, 127, 0, cv2.THRESH_TOZERO)
print(t)

# print("m1 shape:", m1.shape)  # h, w, channel
# print("m shape:", m1.shape[:2])
cv2.imshow("cv2.threshold", m2)
# cv2.imshow("Image M2 B", m2[:, :, 0])
# cv2.imshow("Image M2 G", m2[:, :, 1])
# cv2.imshow("Image M2 R", m2[:, :, 2])

# cv2.THRESH_OTSU => 自動計算門檻值來做二值化，可配合其他方法使用
# 只接受單一通道的色彩空間 => 只接受灰階圖
# 建立m3全白的彩色圖
m3 = np.full(m1.shape, 255, np.uint8)
# BGR分開計算
t, m3[:, :, 0] = cv2.threshold(m1[:, :, 0], 127, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
print(t)
t, m3[:, :, 1] = cv2.threshold(m1[:, :, 1], 127, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
print(t)
t, m3[:, :, 2] = cv2.threshold(m1[:, :, 2], 127, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
print(t)
cv2.imshow("cv2.THRESH_OTSU", m3)

m4 = np.full(m1.shape, 255, np.uint8)
# adaptiveThreshold => 自動計算門檻值，將整張圖像分 成數個小區塊分別去計算
# 結果圖像 =cv2.adaptiveThreshold( 圖像變數,最大值, 方法一, 方法二, 區塊大小, 微調值)
# 區塊大小：只能為小於10基數：3,5,7,9
# 微調值：0 -> 不調整
m4[:, :, 0] = cv2.adaptiveThreshold(m1[:, :, 0], 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 3, 0)
m4[:, :, 1] = cv2.adaptiveThreshold(m1[:, :, 1], 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 5, 0)
m4[:, :, 2] = cv2.adaptiveThreshold(m1[:, :, 2], 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 9, 0)
cv2.imshow("adaptiveThreshold", m4)
# cv2.imwrite("gooooogle.png", m4)

##### 影像邊緣偵測 #####
# 透過一大一小的門檻值，來計算圖象中的邊線Canny
m5 = cv2.Canny(m1, 200, 50)
cv2.imshow("Canny", m5)
# cv2.imwrite("gooooogle5.png", m5)

##### 影像模糊化 #####
# 平均值模糊法(統計範圍內的色彩值平均) blur
# 結果圖像=cv2.blur(圖像變數,範圍大小)  範圍大小 -> Tuple類型:(寬, 高)
m6 = cv2.blur(m1, (15, 5))
cv2.imshow("blur", m6)

# 中值模糊法(將處理範圍內的色彩值做排序，取順序在中間的)
# 處理數量 只能基數
# 取中值有可能丟掉很多數字，讓原圖不見
m7 = cv2.medianBlur(m1, 9)
cv2.imshow("medianBlur", m7)

##### 影像銳利化 #####
# 直方圖均衡化法: 結果圖像=cv2.equalizeHist(圖像變數) 只接受單一通道色彩空間
m8 = np.full(m1.shape, 255, np.uint8)
m8[:, :, 0] = cv2.equalizeHist(m1[:, :, 0])
m8[:, :, 1] = cv2.equalizeHist(m1[:, :, 1])
m8[:, :, 2] = cv2.equalizeHist(m1[:, :, 2])
cv2.imshow("equalizeHist", m8)

####### 形態學 #######
# 侵蝕(色彩值低的會侵蝕色彩值高的): 結果圖像=cv2.erode(圖像變數, 結構陣列)
# 結構陣列 -> np.ones(範圍大小); 範圍大小 -> Tuple類型:(寬, 高)
m9 = cv2.erode(m1, np.ones((2, 2)))
cv2.imshow("cv2.erode", m9)
# 膨脹(色彩值高的會侵蝕色彩值低的) : 結果圖像=cv2.dilate(圖像變數, 結構陣列)
# 結構陣列 -> np.ones(範圍大小); 範圍大小 -> Tuple類型:(寬, 高)
m10 = cv2.dilate(m1, np.ones((3, 3)))
cv2.imshow("cv2.dilate", m10)

# 結果圖像=cv2.morphologyEx(圖像變數, 方法, 結構陣列)
# • cv2.MORPH_OPEN:先執行侵蝕後執行膨脹 (亮的會被清掉)
# • cv2.MORPH_CLOSE:先執行膨脹後執行侵蝕 (暗的會被清掉)
# • cv2.MORPH_GRADIENT:執行膨脹與侵蝕產生的變化差
# 結構陣列 -> np.ones(範圍大小); 範圍大小 -> Tuple類型:(寬, 高)
m11 = cv2.morphologyEx(m1, cv2.MORPH_OPEN, np.ones((9, 9)))
cv2.imshow("cv2.morphologyEx", m11)

###### 取得輪廓 ######
# 輪廓點, 輪廓階層資料=cv2.findContours(圖像變數(灰階圖像),類型, 方法)
# EX: cv2.threshold前處理

m12 = cv2.cvtColor(m3, cv2.COLOR_BGR2GRAY)
a, b = cv2.findContours(m12, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print(a)
# print(b)
cv2.imshow("m3 COLOR_BGR2GRAY", m12)

# 繪製輪廓: cv2.drawContours(圖像變數, 存取全部輪廓的變數, 要繪製的輪廓索引, 顏色,粗細)
m13 = np.full(m1.shape, 255, np.uint8)
cv2.drawContours(m13, a, -1, (255, 0, 0), 1)
cv2.imshow("drawContours", m13)

# m14 = cv2.imread("0903_field.jpg", 0)
# cv2.imshow("Field", m14)
# c, d = cv2.findContours(m14, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# m15 = np.full(m14.shape, 255, np.uint8)
# cv2.drawContours(m15, c, -1, (0, 0, 255), 1)
# cv2.imshow("Field Contours", m15)


# 取得包覆指定輪廓點的最小正矩形:
# X座標, Y座標, 寬度, 高度 =cv2.boundingRect(指定的輪廓)

m16 = np.full(m3.shape, 255, np.uint8)
# print(m16.shape)
'''
cv2.rectangle:
https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html?highlight=rectangle#cv2.rectangle
'''

for d in a:
    x, y, w, h = cv2.boundingRect(d)
    print(x,y,w,h)
    if x < y*2:
        cv2.rectangle(m16, (x, y), (x + w, y + h), (0, 0, 255), 1)
cv2.imshow("rectangle", m16)
# cv2.imshow("rectangle2", m3[])



# if w>h*2:
#     cv2.rectangle(m16,(x,y),(x+w,y+h),(0,0,255),1)
#     cv2.imshow("rectangle", m16)


cv2.waitKey(0)
cv2.destroyAllWindows()
