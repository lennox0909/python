import requests
import codecs

p = requests.get(
    "https://www.ntub.edu.tw/",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Referer": "https://www.ntub.edu.tw/"
    },
    params={
        "Lang":"en"
    }
)
print(p.status_code)

for i in p.headers:
    print(i)

# print(p.headers)
f=codecs.open("0821_spider/1.html","w","utf8")
f.write(p.text)
f.close()
# print(p.text)