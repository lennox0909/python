from bs4 import BeautifulSoup
import requests
import prettytable

w = prettytable.PrettyTable(["縣市", "氣溫"])
w.align = "l"

url = "https://www.cwb.gov.tw/V7/forecast/f_index.htm?_=1566876088218"
p = requests.get(url)
p.encoding = "utf8"
# print(p.text)

x = BeautifulSoup(p.text, features="html.parser")
big01 = x.find("div", class_="big01").find_all("td")
big03 = x.find("div", class_="big03").find_all("td")

t01 = []
for a2 in big01:
    a3 = a2.find("a").text
    t01.append(a3)

t02 = []
for a2 in big03:
    a3 = a2.find("a").text
    t01.append(a3)

all_table = t01 + t02
# print(all_table)

city = []
for i in range(0, len(all_table),4):
    city.append(all_table[i])
# print(city)

temp =[]
for i in range(1, len(all_table),4):
    temp.append(all_table[i])
# print(temp)
for i in range(0,len(city)):
    row = []
    row.append(city[i])
    row.append(temp[i])
    w.add_row(row)

print(w)


#
#
#
# for i in range(0, len(city)):
#     city2 = []
#     ii = i % 4
#     city2.append(city[i])
#     if ii == 0:
#         list1.append(city2)
#         city2 = []
# print(list1)

# print(list1)
# city = ""
# for a4 in a3:
#     city += a4
# print(city)

# print(a1)
# a2 = x.find("div", class_="big03")
# print(a2)
