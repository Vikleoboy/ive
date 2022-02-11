from random import  randint

lst = []
till = int(input())
how_much = int(input())
num = 0
while num <= how_much :
    lst.append(randint(0,till))
    num += 1
print(lst)