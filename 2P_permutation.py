def permutation(string):
    if len(string)==1:
        return[string]


    perms=permutation(string[1:]) 
    results=[]
    char=string[0]

    for perm  in perms:
        for i in range(len(perm)+1):
            results.append(perm[:i]+ char + perm[i:])

    return results   

print(permutation('ABC'))       