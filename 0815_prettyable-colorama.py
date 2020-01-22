
import prettytable

p=prettytable.PrettyTable(["AAA","BBB","第三欄"],encoding="utf8")
p.add_row([1,2,3])
p.add_row([4,5,6])
p.add_row([7,8,9])
p.align["AAA"]="r"
p.align["BBB"]="r"

print(p)
print()


import colorama

print(colorama.Fore.RED+"ABC"+colorama.Fore.RESET+"DEF")
print(colorama.Back.RED+"ABC"+colorama.Back.RESET+"DEF")
print(colorama.Style.BRIGHT+"ABC"+colorama.Style.NORMAL+"DEF")
