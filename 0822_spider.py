import requests
import codecs
import csv
import json
import io
import prettytable

p = requests.get(
    "http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-G01086-002"
)
p.encoding = "utf8"
j = json.loads(p.text)

for a in j["result"]["records"]:
    print(a["breau"],a["p_count"])
    # print(a)
    # for b in a:
    #     print(b)


    # for b in a["records"]:
    #     print(b)
    #     for c in b["7"]:
    #         print(c)
# a = j["result"]["records"]["7"]
# print(a)


#
# r.encoding="utf8"
# print(r.text)

# f = io.StringIO(p.text)  # 把讀到的資料轉成檔案串流
#
#
# result = list(csv.reader(f))  # 剖析CSV格式
# print(result)
#
# # 用prettytable排版結果資料
# w = prettytable.PrettyTable(result[1], encoding="big5")
# for i in result[2:]:
#     w.add_row(i)
# print(w)  # 顯示結果
#
# s = codecs.open("result.txt","w")
# s.write(str(w))
# s.close()
