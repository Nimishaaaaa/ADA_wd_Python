#code to find the duplicate in the list
def dupli(lis):
    dupli=[]                                               #empty list to store all duplicates
    for i in range(len(lis)):
        k=i+1
        for j in range(k,len(lis)):                        #ith value will be compared from i+1 to n( 1 will be compared from 4 to 8)
            if lis[i]==lis[j] and lis[i] not in dupli:    #if i is repeated more than 1 time, it will be ignored through second cond'
                dupli.append(lis[i])
    return  dupli

            
            
l1=[1,4,5,4,6,7,8,8]
print(dupli(l1))

