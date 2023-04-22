#linear search

#for this we need to create our own function
#ex - search the given number in list
pos = -1

def search(list,n):
    c=0
    for i in list:
        if i == n:
            globals()['pos'] = c
            return True
        c += 1
    return False

list = [2,6,7,8,4,9,8]

n = 10

if search (list,n):
    print("Found at",pos)
else:
    print("Not Found")