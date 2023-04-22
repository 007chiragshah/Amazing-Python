#Linear search is good but what if you have 1000 lines of code and required value is after 800 then this will take time.
#for binary search need to perform steps as below:
#1. the list should be sorted
#2. Find the lower bound (leasr index) and upper bound (highest index)
#3. Find the mid value as (l+u)//2
#4. Then check if the given value is equals to mid value or not
#5. If yes then print the value with position
#6. If not then check if the value is larger than the mid value or not and accordingly change the mid value
#7. if it's lower then shift your Upper bond to mid-1 value as mid value already get checked
#8. if it's larger than shift your lower bound to mid+1.
#9. then again find the new mid value and continue the activity untill we found the match

#ex
pos = -1
def search(list,n):
    l=0              #defining the lower bound
    u=len(list)-1    #defining the upper bound

    while l <= u:
        mid = (l + u) // 2  # finding the mid value by int devision means by using //
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;

    return False

list = [4,6,8,10,50,51,100,150,200,250,300,350,400,60000]
n = 111

if search(list, n):
    print("Found at: ",pos+1)
else:
    print("Not Found")