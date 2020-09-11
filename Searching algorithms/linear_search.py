# linear search works both on sorted/unsorted array
# <---time complexity--->
# best    average   worst
# O(1)      O(n)     O(n)

def linear(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            return 1
    return 0

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    key=int(input())
    if linear(arr,n,key)==1:
        print("YES")
    else:
        print("NO")