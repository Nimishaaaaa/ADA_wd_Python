class adj_matrix:
    def __init__(self, vertices):
        self.vertices=vertices
        self.matrix=[[0 for i in range(vertices)] for i in range(vertices)]         #if matrix of n*n size 4

    def add_edge(self,v1,v2):                 #check if there is edge or not     
        if (v1==v2):
            return
        self.matrix[v1][v2]=1
        self.matrix[v2][v1]=1
        
    def remove_edg_edg(self, v1, v2):           #function for removal of function
        if self.matrix[v1][v2] > 0:
            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0
        
    def print_matrix(self):                     #to print matrix row wise
        for row in self.matrix:
            print(row)
        print("\n")

vertices = int(input("No of vertices: "))            #taking no of vertices as n for n*n matrix

m=adj_matrix(vertices)

# Rows as input
for i in range(vertices):
    row = input(f"Enter row {i}: ").split(" ")                       #converting list of strings into list of numbers
    
    row = [int(item) for item in row] 
    for i in range(len(row)):
        if row[i]!= 0:
            m.add_edge(1,i)

m.print_matrix()
