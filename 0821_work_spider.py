import requests

r = requests.get(
    "http://teaching.bo-yuan.net/test/requests/"
)

g = requests.get(
    "http://teaching.bo-yuan.net/test/requests/?action=A"
)
d = requests.delete(
    "http://teaching.bo-yuan.net/test/requests/?action=A"
)

post = requests.post(
        "http://teaching.bo-yuan.net/test/requests/?action=A",
        data={"id":"a"}
)
put = requests.put(
        "http://teaching.bo-yuan.net/test/requests/?action=A",
        data={
            "id":"a",
            "XXX":"XXX"
              }
)

put2 = requests.put(
        "http://teaching.bo-yuan.net/test/requests/?action=A",
        data={
            "id":"a",
            "name":"Leno"
              }
)


patch = requests.patch(
        "http://teaching.bo-yuan.net/test/requests/?action=A",
        data={
            "id":"a",
            "name":"Leno",
            "xxx":"xxx"}

)

patch2 = requests.patch(
        "http://teaching.bo-yuan.net/test/requests/?action=A",
        data={
            "id":"a",
            "name":"Leno",
            "address":"Taipei"}

)

post2 = requests.post(
        "http://teaching.bo-yuan.net/test/requests/?action=A",
        data={
            "id":"a",
            "name":"Leno",
            "address":"Taipei",
            "email":"leno@mail.com"
        }

)

r.encoding="utf8"
g.encoding="utf8"
d.encoding="utf8"
post.encoding="utf8"
put.encoding="utf8"
put2.encoding="utf8"
patch.encoding="utf8"
patch2.encoding="utf8"
post2.encoding="utf8"

print(r.text)
print(g.text)
print(d.text)
print(post.text)
print(put.text)
print(put2.text)
print(patch.text)
print(patch2.text)
print(post2.text)
