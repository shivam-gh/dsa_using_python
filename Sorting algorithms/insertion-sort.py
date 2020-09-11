# efficient algorithm for sorting almost sorted array/list
# <---time complexity--->
# best    average   worst
# O(n)     O(n^2)   O(n^2)

def insertion(arr,n):
    for k in range(1,n):
        temp=arr[k]
        j=k-1
        while j>=0 and arr[j]>=temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    insertion(arr,n)
    print(*arr)