__author__ = 'marc.legendre'

mylist = [1, 2, 3, 4]
mytuple = (1, 2, 3, 4)
_num = 0

print("hello python \n")

for item in mylist:
    print(item)

for item in mytuple:
    print(item)

_num = int(input("compare any number you want: "))

if _num < 4:
    print(_num, " is less than 4")
else:
    print(_num, " is greater than 4")
