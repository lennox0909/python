# 連結MySQL
import pymysql

conn = pymysql.connect(
    host="localhost",
    port=33306,
    user="root",
    passwd="",
    db="0820db",
    charset="utf8"
)

# 取得指令操作變數:
cmd = conn.cursor()

# 傳送SQL指令
# 指令操作變數.execute(SQL指令, 要帶入SQL中的變數)

# x = {
#     "name":"ppp",
#     "email":"ppp",
#     "address":"ppp"
# }
# cmd.execute(
#     "insert into `member`(`name`,`email`,`address`) values(%(name)s,%(email)s,%(address)s)",
#     x)

# name="www"
# email="www"
# address="www"
'''==='''

# name = input("請輸入姓名：")
# birth = input("請輸入生日：")
# address = input("請輸入地址：")
#
# cmd.execute(
#     "insert into `member`(`name`,`birth`,`address`) values(%s,%s,%s)",
#     (name, birth, address))
#
# # 如果是新增、刪除或修改指令需再執行
# conn.commit()
# print("剛剛新增的ID：", cmd.lastrowid)

'''==='''

cmd.execute("select * from `member`")
x = cmd.fetchall()
for i in x:
    print(i)
    # for j in i:
    #     print(i[j])


# 關閉MySQL連線:
conn.close()
