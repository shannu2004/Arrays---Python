def findCommon(a1,a2,a3):
    n1=len(a1)
    n2=len(a2)
    n3=len(a3)
    i=j=k=0
    while i<n1 and j<n2 and k<n3:
        if a1[i]==a2[j] and a2[j]==a3[k]:
            print(a1[i],end=" ")
            i+=1
            j+=1
            k+=1
        elif a1[i]<a2[j]:
            i+=1
        elif a2[j]<a3[k]:
            j+=1
        else:
            k+=1


a1=[1,5,10,20,40,80]
a2=[2,5,6,7,8,9,20,88]
a3=[5,20,11,22,33,44,55,66]
findCommon(a1,a2,a3)
