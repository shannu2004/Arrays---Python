def findMissing(arr,n):
    temp=[0]*(n+1)
    for i in range(0,n):
        temp[arr[i]-1]=1
    for i in range(0,n+1):
        if(temp[i]==0):
            ans=i+1
    print(ans)
arr=[1,2,3,5]
n=len(arr)
findMissing(arr,n)
