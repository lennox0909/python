import time
import os

x=["A","B","C"]
i = 0

while True:
    os.system("clear")
    print(time.time())
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    # print(x[i])
    # i+=1
    # i%=3
    time.sleep(1)

# import prettytable
#
# p=prettytable.PrettyTable(["第一欄","第二欄","第三欄"],encoding="utf8")
# p.add_row([1,2,3])
# p.add_row([4,5,6])
# p.add_row([7,8,9])
# # p.align["AAA"]="r"
# # p.align["BBB"]="r"
#
# print(p)





# print(colorama.Fore.RED+"ABC"+colorama.Fore.RESET+"DEF")
# print(colorama.Back.RED+"ABC"+colorama.Back.RESET+"DEF")
# print(colorama.Style.BRIGHT+"ABC"+colorama.Style.NORMAL+"DEF")
