'''Mac用預設瀏覽器開啟google'''

import os
p = os.popen("open "+"https://www.google.com.tw/")
x = p.read()
print(x)
