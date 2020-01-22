import cv2
import numpy as np

m = cv2.imread("2018_0101.png", 1)
cv2.imshow("Image M", m)
# print("m shape:", m.shape)  # h, w, channel
print("m shape:", m.shape[:2])

leno = cv2.imread("LenoDesign.png", 1)
cv2.imshow("Image Leno", leno)
print("leno shape:", leno.shape)
# print("leno shape:", leno.shape[:2])

range = 40
leno_filter = cv2.inRange(leno,
                          (max(255 - range, 0), max(95 - range, 0), max(35 - range, 0)),
                          (min(255 + range, 255), min(95 + range, 255), min(35 + range, 255)))
leno_filterBGR = cv2.cvtColor(leno_filter, cv2.COLOR_GRAY2BGR)
cv2.imshow("leno_filterBGR", leno_filterBGR)
print("leno_filterBGR:", leno_filterBGR.shape)

m_mark = m.copy()
m_mark[0:97, 0:336] = cv2.add(m[0:97, 0:336], leno_filterBGR)
cv2.imshow("Image m_mark", m_mark)

# mf = cv2.flip(m, -1)
# m2 = np.full(m.shape, (50, 50, 50), np.uint8)


# leno2 = cv2.resize(leno,(m.shape[1], m.shape[0]))


# cv2.imshow("Image Leno-a", leno)
# m_cut = m[20:200, 50:500]  # h, w
# m[0:96, 0:335] = leno[0:96, 0:335]
# m_logo2 = cv2.subtract(leno, m[10:96, 10:335])

# m3 = cv2.bitwise_xor(m, m2)

# m4 = cv2.imread("2018_0102.png", 1)
# m4c = cv2.resize(m4, (m.shape[1], m.shape[0])) # w,h
# m5 = cv2.absdiff(m, m4c)

# m6 = m + m4c*2


# cv2.imshow("Image M-J", m[::2, ::2])


# cv2.imshow("Image leno2", leno2)
# cv2.imshow("Image M-Cut", m_cut)

# cv2.imshow("Image M4", m4)
# cv2.imshow("Image M4c", m4c)
# cv2.imshow("Image M5", m5)
# cv2.imshow("Image M6", m6)
# cv2.imshow("Image M-flip", mf)
cv2.waitKey(0)
cv2.destroyAllWindows()
