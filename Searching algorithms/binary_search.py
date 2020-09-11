# binary search can be implemented only on sorted array/list 
# <----time complexity---->
# best    average    worst
# O(1)   O(log n)   O(log n)

def binary(arr,beg,end,key):
    if beg<=end:
        mid=(beg+end)//2
        if arr[mid]==key:
            return 1
        elif arr[mid]>key:
            return binary(arr,beg,mid-1,key)
        else:
            return binary(arr,mid+1,end,key)
    else:
        return -1

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    key=int(input())
    if binary(arr,0,n-1,key)==1:
        print("YES")
    else:
        print("NO")
