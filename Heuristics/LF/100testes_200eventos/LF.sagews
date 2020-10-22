from sage.all import Graph, matrix
import time
import sys

def my_read(data):
    f = open(data, 'r')
    f = f.read() #Leitura do Arquivo
    f = f.split("\n") #cria lista de evento por linha do arquivo
    graph = []
    for i in f[:-1]:
        dupla = i.split(",")
        graph.append((dupla[0],dupla[1]))
    return graph

def lf(g):
    vertex = []
    count1 = 0
    inicio = time.time()
    for v in g:
        count1 += len(g)
        vertex.append([v,g.degree(v),g.neighbors(v)])
    vertex.sort(key=lambda x: x[1], reverse = True)

    colour = [[vertex[0][0]]]

    aux = vertex.pop(0)

    count2 = 0
    for v in vertex:
        verify = False
        for c in colour:
            count2 += len(colour)
            intersec = set(c).intersection(set(v[2]))
            if intersec == set():
                c.append(v[0])
                verify = True
                break
        if verify == False:
            colour.append([v[0]])
    fim = time.time()

    #print("Tempo LF: ",fim - inicio)

    #inicio2 = time.time()
    #print(g.chromatic_number())
    #fim2 = time.time()
    #print("Tempo: ",fim2 - inicio2)
    
    print(len(colour), ":", count1+count2, ":", count1, ":", count2, ":", fim-inicio)

input = sys.argv[1:][0]
data = my_read(input)
g = Graph()
g.add_edges(data)
lf(g)









