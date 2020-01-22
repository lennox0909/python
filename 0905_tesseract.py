import pytesseract as pt
import cv2
from pyzbar import pyzbar
import numpy as np

##### ＯＣＲ文字辨識 #####
m1 = cv2.imread("jandi.png", 1)  # 0 => gray
cv2.imshow("Image M1", m1)
# 辨識結果=pt.image_to_string(圖片變數, 語言包名稱, 設定值)
txtEn = pt.image_to_string(m1, "eng", "")
print(txtEn)

##### 條碼辨識 #####
# 結果變數=pyzbar.decode(圖像變數)
# 串列(list)類型，每個索引 值指向一個條碼
'''
結果變數中各個索引值的內容屬性: 
type:條碼類型  data:結果文字
由於是日本人寫的，所以如果要顯示UTF-8的中文必須:
decode成UTF-8後再encode成sjis，最後再decode成UTF-8
'''
m2 = cv2.imread("qrcode2.png", 0)  # 0 => gray
cv2.imshow("qrcode2", m2)
m2r = pyzbar.decode(m2)
print(m2r)


##### 辨識 #####
'''
分類器:
    控制變數=cv2.CascadeClassifier(分類器文件)
辨識目標:
    結果變數=控制變數.detectMultiScale(
圖像變數, minNeighbors=檢測門檻數, minSize=最小尺寸)
'''
m3 = cv2.imread("frontalface.jpg", 1)  # 0 => gray

p = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
r = p.detectMultiScale(m3, minNeighbors=3, minSize=(30, 30))
# print(r)
for x, y, w, h in r:
    cv2.rectangle(m3, (x,y), (x+w, y+h), (0,0,255), 3)
cv2.imshow("frontal face", m3)

cv2.waitKey(0)
cv2.destroyAllWindows()
