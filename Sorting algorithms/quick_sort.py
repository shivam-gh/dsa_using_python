# <-----time complexity----->
#   best     average    worst
# O(nlogn)   O(nlogn)   O(n^2)

def partition(arr,beg,end):
    pivot=arr[end]
    i=beg
    for j in range(beg,end):
        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[end]=arr[end],arr[i]
    return i

def quicksort(arr,beg,end):
    if beg<end:
        pi=partition(arr,beg,end)
        quicksort(arr,beg,pi-1)
        quicksort(arr,pi+1,end)


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    quicksort(arr,0,n-1)
    print(arr)