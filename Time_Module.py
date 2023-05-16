import time

#if we want to know how much time taken by our code to run then need to use time module

initial = time.time()   #this will store the time when prog start
i=0
while i < 5:
    print("chirag")
    i+=1
print(f"while loop has taken {time.time() - initial} to run")


initial2 = time.time()
for i in range(5):
    print("Chirag")
print(f"For loop has taken {time.time() - initial2} to run")


