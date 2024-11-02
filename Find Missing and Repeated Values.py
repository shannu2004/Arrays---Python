def Missingrepeating(arr):
    n=len(arr)
    count=[0]*(n+1)
    for num in arr:
        count[num]+=1
    missing=-1
    repeating=-1
    for i in range(1,n+1):
        if count[i]==2:
            repeating=i
        elif count[i]==0:
            missing=i
    return missing, repeating
arr=[3,1,3]
print(Missingrepeating(arr))
