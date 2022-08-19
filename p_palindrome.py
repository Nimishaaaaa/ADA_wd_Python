class un_palindrome:
    def __init__(self,str):
        self.str1=str
        self.unique_set=set()
    def sub_st(self):
        i = 0
        while i <len(self.str1):
            j = len(self.str1) - 1
            while (j>i):
                if self.str1[i] == self.str1[j]:
                    if self.is_palindrome(i,j):
                        self.unique_set.add(self.str1[i:j+1])
                        i = (i+j)//2
                        break
                j -= 1
            i+=1
    def is_palindrome(self,s_index,e_index):
        while(s_index<=e_index):
            if(self.str1[s_index]==self.str1[e_index]):
                s_index+=1
                e_index-=1
            else:
                return False
        return True
string="ASISAPEPART"
pldrome1=un_palindrome(string)
pldrome1.sub_st()
print(pldrome1.unique_set)