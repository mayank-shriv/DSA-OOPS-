# First merge two sorted array
def merge(list1,list2):
    result=[]
    p,q=0,0
    n,m= len(list1),len(list2)
    while (p<n and q<m):
        if list1[p]<=list2[q]:
            result.append(list1[p])
            p+=1   
        else:
            result.append(list2[q])    
            q+=1   
    if p<n:
        while p<n:
                result.append(list1[p])
                p+=1
    else:
        while q<m:
                result.append(list2[q])
                q+=1

    print(list(set(result)))


list1 = [1,5,9,109,244]
list2 = [8,9,10,20,120]
merge(list1,list2)


# Merge Sort 

