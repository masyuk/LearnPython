import sys
putdofila = "takogo_fila_net.txt"

while True:
    try:
        myfile = open(putdofila, mode="r", encoding="utf_8")
    except Exception:
        print("File ne nayden")
        print(sys.exc_info()[1])
        putdofila = input("Enter name file: ")
    else:
        print(myfile.read())
        sys.exit()
    finally:
        print("Proga is cose")