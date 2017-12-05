name = input("Enter your name ")
print('Hi ' + name)
#input всешжа читает строки

num1 = input('Enter first num ')
num2 = input('Enter second num ')
print(int(num1)+int(num2))

while True:
    mymess = input('Enter pass')
    if mymess == 'pass': break
    print('Password incorrect')