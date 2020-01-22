import colorama
import time
import os
# import random

# sign = ["▲","▇","✿"]
i = 0
colorama.init(True)
while True:
    os.system("clear") # with Mac OS
    # k = random.randint(0, 2)
    # s = sign[k]
    i += 1
    if i == 10:
        i = 0

    if i < 6:
        print(colorama.Fore.RED + "▇")
        print(i)
    elif i == 6:
        print(colorama.Fore.YELLOW + "   ▇")
        print(i)
    elif i > 6:
        print(colorama.Fore.GREEN + "      ▇")
        print(i)
    time.sleep(1)


