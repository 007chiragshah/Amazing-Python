#There are many sortin method and all sorting method have one common thing is swaping
#So for buuble sort we do following steps :
#first compare two numbers
#and make sure that smaller one will be the firstand if not we can do it by swapping
#and check this to last iteration then we get the biggest number at the end
#now do this iteration  same as the length of list minus 1
#for ex if we have length is 6 then will get the correct output in 5 iteration
#for this we need to 2 loops 1 for outer iteration and one for inner iteration

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp

nums = [5,3,8,6,7,2]

sort(nums)
print(nums)