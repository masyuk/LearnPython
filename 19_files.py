inputfile = "files\myfile.txt"
outputfile = "files\mynewfile.txt"

myfile1 = open(inputfile, mode='r', encoding='utf_8')
myfile2 = open(outputfile, mode='w', encoding='utf_8')
# w - write
# r - read
# a - add
# r+ - read and write

# print(myfile.read())

for num, line in enumerate(myfile1, 1):
    if "string" in line:
        print(str(num) + " " + line.strip())
        myfile2.write(line)

myfile1.close()
myfile2.close()