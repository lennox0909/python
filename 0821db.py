'''run in MacOS'''

import pymysql
import os
import prettytable

conn = pymysql.connect(
    host="localhost",
    # port=3306,
    user="root",
    passwd="",
    db="0821db",
    charset="utf8"
)
cmd = conn.cursor()

r = "-1"
while r != "0":
    if r == "1":
        os.system("clear")
        cmd.execute(
            "SELECT * FROM `member` LEFT JOIN `telephone` on `member`.`id`=`telephone`.`id_member` ORDER BY `member`.`id` ASC")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["流水編號", "姓名", "生日", "地址", "電話"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            del row[4]
            del row[-1]
            p.add_row(row)
        p.align["姓名"] = "l"
        p.align["地址"] = "l"
        print(p)

    elif r == "2":
        name = input("請輸入姓名：")
        birth = input("請輸入生日：")
        address = input("請輸入地址：")
        cmd.execute(
            "insert into `member`(`name`,`birthday`,`address`) values(%s,%s,%s)",
            (name, birth, address))
        conn.commit()

    elif r == "3":
        os.system("clear")
        cmd.execute(
            "SELECT * FROM `member` LEFT JOIN `telephone` on `member`.`id`=`telephone`.`id_member` ORDER BY `member`.`id` ASC")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["流水編號", "姓名", "生日", "地址", "電話"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            del row[4]
            del row[-1]
            p.add_row(row)
        p.align["姓名"] = "l"
        p.align["地址"] = "l"
        print(p)
        reInput = input("請選擇你要修改的資料：")
        cmd.execute("select * from `member`")
        name = input("請輸入姓名：")
        birth = input("請輸入生日：")
        address = input("請輸入地址：")

        cmd.execute(
            "update `member` set `name`='" + name + "',`birthday`='" + birth + " ',`address`=' " + address + "' where `id`='" + reInput + "'")
        conn.commit()

    elif r == "4":
        os.system("clear")
        cmd.execute(
            "SELECT * FROM `member` LEFT JOIN `telephone` on `member`.`id`=`telephone`.`id_member` ORDER BY `member`.`id` ASC")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["流水編號", "姓名", "生日", "地址", "電話"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            del row[4]
            del row[-1]
            p.add_row(row)
        p.align["姓名"] = "l"
        p.align["地址"] = "l"
        print(p)
        inDelete = input("請選擇你要刪除的資料：")
        cmd.execute("delete from `member` where `id` = '" + inDelete + "'"
                    )
        conn.commit()

    elif r == "5":
        os.system("clear")
        cmd.execute(
            "SELECT * FROM `member` LEFT JOIN `telephone` on `member`.`id`=`telephone`.`id_member` ORDER BY `member`.`id` ASC")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["流水編號", "姓名", "生日", "地址", "電話"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            del row[4]
            del row[-1]
            p.add_row(row)
        p.align["姓名"] = "l"
        p.align["地址"] = "l"
        print(p)
        inPhone = input("請選擇要添加電話的會員編號：")
        noPhone = input("請輸入電話號碼：")

        cmline = "insert into `telephone`(`tel`, `id_member`) values('%s','%s')" % (noPhone, inPhone)
        cmd.execute(cmline)
        aaa = cmline.replace("\\", "")
        print(aaa)
        conn.commit()

    elif r == "6":
        os.system("clear")
        cmd.execute(
            "SELECT * FROM `member` LEFT JOIN `telephone` on `member`.`id`=`telephone`.`id_member` ORDER BY `member`.`id` ASC")
        x = cmd.fetchall()
        p = prettytable.PrettyTable(["流水編號", "姓名", "生日", "地址", "電話"], encoding="utf8")
        for i in x:
            row = []
            for j in i:
                row.append(str(j))
            del row[4]
            del row[-1]
            p.add_row(row)
        p.align["姓名"] = "l"
        p.align["地址"] = "l"
        print(p)
        inPhone = input("請選擇要刪除電話的會員編號：")

        cmd.execute(
            "SELECT * FROM `telephone` WHERE `id_member` =" + inPhone)
        # SELECT * FROM `telephone` WHERE `id_member` = 21
        x2 = cmd.fetchall()
        p2 = prettytable.PrettyTable(["流水編號", "電話"], encoding="utf8")
        for i in x2:
            row = []
            for j in i:
                row.append(str(j))
            del row[-1]
            p2.add_row(row)
        print(p2)
        inPhone2 = input("請選擇要刪除電話的流水編號：")
        cmd.execute("delete from `telephone` where `id` = '" + inPhone2 + "'"
                    )
        conn.commit()

    print("(0) 離開程式")
    print("(1) 顯示會員列表")
    print("(2) 新增會員資料")
    print("(3) 更新會員資料")
    print("(4) 刪除會員資料")
    print("(5) 新增會員的電話")
    print("(6) 刪除會員的電話")
    r = input("指令：")

conn.close()
