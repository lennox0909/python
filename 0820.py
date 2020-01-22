x = 4

if x == 0:
    print('A')
elif x == 1:
    print('B')
elif x == 2:
    print('C')
elif x == 3:
    print('D')
elif x == 4:
    print('E')
else:
    print('F')

# 少用elif, 以下兩種方法...

Leno = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}

if x in Leno:
    print(Leno[x])
else:
    print("F")

# 用try/except來替代
try:
    newx = Leno[x]
except KeyError as e:
    newx = "F"
print('newx=', newx)

# 9x9 乘法表

for num in range(1, 9 + 1):
    for mul in range(1, 9 + 1):
        print("{}x{}={:2s} ".format(num, mul, str(num * mul)), end='')
    print('')

# delete from `member` where `id` = 3
