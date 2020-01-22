'''run in MacOS'''

import pymysql
import os
import prettytable

conn = pymysql.connect(
    host="localhost",
    # port=3306,
    user="root",
    passwd="",
    db="0820db",
    charset="utf8"
)
cmd = conn.cursor()

r = "-1"
while r != "0":
    if r == "1":
        os.system("clear")
        cmd.execute("select * from `member`")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["編號", "姓名", "生日", "地址"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            p.add_row(row)
        p.align["姓名"] = "l"
        p.align["地址"] = "l"
        print(p)

    elif r == "2":
        name = input("請輸入姓名：")
        birth = input("請輸入生日：")
        address = input("請輸入地址：")
        cmd.execute(
            "insert into `member`(`name`,`birth`,`address`) values(%s,%s,%s)",
            (name, birth, address))
        conn.commit()


    elif r == "3":
        os.system("clear")
        cmd.execute("select * from `member`")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["編號", "姓名", "生日", "地址"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            p.add_row(row)
        print(p)
        reInput = input("請選擇你要修改的資料：")
        cmd.execute("select * from `member`")
        name = input("請輸入姓名：")
        birth = input("請輸入生日：")
        address = input("請輸入地址：")
        cmd.execute("update `member` set `name`='" + name + "',`birth`='" + birth + " ',`address`=' " + address + "' where `id`='"+reInput+"'")
        conn.commit()

    elif r == "4":
        os.system("clear")
        cmd.execute("select * from `member`")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["編號", "姓名", "生日", "地址"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            p.add_row(row)
        print(p)
        inDelete = input("請選擇你要刪除的資料：")
        cmd.execute("delete from `member` where `id` = '" + inDelete + "'"
            )
        conn.commit()

    print("(0) 離開程式")
    print("(1) 顯示會員列表")
    print("(2) 新增會員資料")
    print("(3) 更新會員資料")
    print("(4) 刪除會員資料")
    r = input("指令：")

conn.close()