# <-----time complexity------>
#   best     average     worst
# O(nlogn)   O(nlogn)   O(nlogn)

def merge(arr,beg,end,mid):
    leftsize=mid-beg+1
    rightsize=end-mid
    left,right=[],[]

    for i in range(leftsize):
        left.append(arr[beg+i])

    for j in range(rightsize):
        right.append(arr[mid+j+1])

    i,j,k=0,0,beg

    while i<leftsize and j<rightsize:
        if left[i]>=right[j]:
            arr[k]=right[j]
            j+=1
        else:
            arr[k]=left[i]
            i+=1
        k+=1

    while i<leftsize:
        arr[k]=left[i]
        i+=1
        k+=1
        
    while j<rightsize:
        arr[k]=right[j]
        j+=1
        k+=1
  
def mergesort(arr,beg,end):
    if beg==end:
        return
    mid=beg+(end-beg)//2
    mergesort(arr,beg,mid)
    mergesort(arr,mid+1,end)
    merge(arr,beg,end,mid)

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    mergesort(arr,0,n-1)
    print(*arr)
