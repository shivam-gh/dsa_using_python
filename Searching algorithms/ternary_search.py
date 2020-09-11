# Ternary search is similar to the binary search, the only difference is that 
# in binary search, the sorted array is divided into two parts while in ternary search, 
# it is divided into  parts and then you determine in which part the element exists.

# <----time complexity---->
# best    average    worst
# O(1)   O(log n)   O(log n)

def ternary(arr,beg,end,key):
    if beg<=end:
        mid1=beg+(end-beg)//3
        mid2=end-(end-beg)//3
        if arr[mid1]==key:
            return 1
        if arr[mid2]==key:
            return 1
        if arr[mid1]>key:
            return ternary(arr,beg,mid1-1,key)
        elif arr[mid2]<key:
            return ternary(arr,mid2+1,end,key)
        else:
            return ternary(arr,mid1,mid2,key)
    else:
        return -1

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    key=int(input())
    if ternary(arr,0,n-1,key)==1:
        print("YES")
    else:
        print("NO")