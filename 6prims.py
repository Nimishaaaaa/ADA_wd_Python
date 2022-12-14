INF = 9999999 
N = 5

G = [[0, 11, 4, 0, 0],
     [12, 0, 9, 5, 2],
     [4, 6, 0, 0, 3],
     [0, 7, 4, 0, 6],
     [0, 7, 3, 8, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

print("Edge : Weight\n")
while (no_edge < N - 1):
   
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
    