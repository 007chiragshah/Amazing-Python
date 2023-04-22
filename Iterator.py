#Iterator means it will print next by next numbers

nums = [7,8,9,5]

#1st way to print by index number
print(nums[0])    #by using 1 by 1 index number


#2nd way  by for loop

for i in nums:
    print(i)

#3rd way is by Iterator

it =iter(nums)   #converting list to iterator

print(it)      #if we print only it, it will give an only object

#so
print(it.__next__())   #we will use the in built function will print the value
print(it.__next__())   #will print the next value


#Now what if want to create our own iterator with next and iter methods


class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):    #creating iter method
        return self

    def __next__(self):    #creating next method
        if self.num <= 10:    #definig the range to limit the output till 10
            val = self.num
            self.num += 1
            return val
        else:
            raise stopiteration

values = Topten()

for i in values:
    print(i)