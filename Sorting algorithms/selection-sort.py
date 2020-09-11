# <---time complexity--->
# best    average   worst
# O(n)     O(n^2)   O(n^2)

def selection(arr,n):
    for i in range(0,n-1):
        minimum=i
        for j in range(i+1,n):
            if arr[j]<arr[minimum]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    selection(arr,n)
    print(*arr)