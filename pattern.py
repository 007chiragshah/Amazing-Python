'''for i in range(1,5):
    print("#" * i)

for i in range(5,0,-1):
    print('#'* i)

k=1
for i in range(1,5):
    for i in range(k,5):
        print(i,end="")
    print()
    k=k+1

k=1
l=0
a='ABCD'
b='PQR'
for i in range(4):
    for i in a[:k],b[l:]:
        print(i,end="")
    k=k+1
    l=l+1
    print()


num=7
for i in range(2,num):
    if num%i == 0:
        print("Given Num is not a prime num")
        break
else:
    print("Given num is a prime num")
'''