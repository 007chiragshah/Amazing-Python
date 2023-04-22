#in bubble sort we are doing swapping at each iteration and more swapping consumes mote cpu and mem
#so need to swapping once at each iteration we will use selection sort
#in this method we find the min value from list and at last will swap the min value to first

#ex

def sort(nums):
    for i in range(len(nums)-1):
        minpose = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpose]:
                minpose = j

        temp = nums[i]
        nums[i] = nums[minpose]
        nums[minpose] = temp

nums = [5,3,8,6,7,2]

sort(nums)
print(nums)