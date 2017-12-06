import sys
import os #запускать команды доса или линукса

x = len(sys.argv) #длина

if x > 1:
    print(sys.argv[1:])

    if sys.argv[1] == "help":
        print("faq you")

    if sys.argv[1] == "ls":
        os.system("dir")
else:
    print("args not provided")

# ------------------------------ #


