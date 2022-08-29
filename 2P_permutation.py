def permutation(string):
    if len(string)==1:
        return[string]


    perms=permutation(string[1:]) 
    result=[]
    char=string[0]

    for perm  in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+ char + perm[i:])

    return result    

print(permutation('ABC'))       