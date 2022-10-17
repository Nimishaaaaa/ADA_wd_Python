W=int(input("enter the capacity of sack:"))     

wt=input("enter the weight of the items:")              
wt=wt.split()                                                  #split seprates string  inputs into list, seprator:white spaces

wt=[int(i)for i in wt]                                           


profit=input("enter the profit of the")
profit=profit.split()

profit=[int(j) for j in profit]                               #converting string into int


List1=[(wt[i],profit[i])for i in range(0,len(profit))]         #[(10,34), (30,54), (51,56)] list is created using list comprehension
arr=sorted(List1,key=lambda x: x[1],reverse=True)                               #sorted(iterable,key,reverse)   true--desecending
print(arr)


def knapsack(W,arr):
    total_profit=0

    for item in arr:
        if item[0]<=W:
            total_profit=total_profit+item[1]
            W=W-item[0]
    return total_profit

A=knapsack(W,arr)
print(A)

