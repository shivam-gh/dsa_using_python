# <---time complexity--->
#  best   average   worst
# O(n+k)   O(n+k)   O(n+k)

def counting(arr,n):
    maximum=max(arr)
    arr2=[0 for i in range(maximum+1)]
    for i in arr:
        arr2[i]+=1
    for i in range(len(arr2)):
        for _ in range(0,arr2[i]):
            print(i,end=" ")

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    counting(arr,n)