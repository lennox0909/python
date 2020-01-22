import requests
import json
import prettytable
import os


def query(search, page):
    p = requests.get(
        "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + search + "&page=" + page + "&sort=sale/dc",
        headers={
            "Host": "ecshweb.pchome.com.tw",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Referer": "https://ecshweb.pchome.com.tw/search/v3.3/?q=PC",
            "Cookie": "ECC=2752f4b0986bf85b5a5e9b810032ba7e257d9401.1566461528; _gcl_au=1.1.1321705795.1566461530; gsite=shopping; _ga=GA1.3.1054014464.1566461531; _gid=GA1.3.530024540.1566461531; venguid=26faaa5b-9890-44c3-99f0-417c8346eb1d.wg1-mfrp20190822; _gat_UA-115564493-1=1; _fbp=fb.2.1566461530978.1209721921; U=9be237e08db2f6663e123d10b40913f5232f631c; ECWEBSESS=3bc8e04aca.16dae7ebef34465e8429c2ff07996585541f4e5c.1566461551",
            "TE": "Trailers"
        }
    )
    p.encoding = "utf8"
    j = json.loads(p.text)
    return j

os.system("clear")
search = input("請輸入關鍵字：")
page = "1"

while True:
    os.system("clear")
    j2 = query(search, page)
    w = prettytable.PrettyTable(["品名","價格","圖片","URL"])
    w.align = "l"
    for a in j2["prods"]:
        row = []
        # print(a["name"], "NT$"+str(a["price"]))
        row.append(a["name"])
        row.append("NT$ " + str(a["price"]))
        row.append("https://b.ecimg.tw" + a["picB"])
        row.append("https://24h.pchome.com.tw/prod/" + a["Id"])
        # print(row)
        w.add_row(row)
    print(w)
    page = input("請輸入頁碼(輸入0離開)：")
    if page =="0":
        break
