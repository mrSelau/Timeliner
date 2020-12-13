from sage.all import Graph, matrix
import time
import sys
from random import randint

def my_read(data):
    f = open(data, 'r')
    f = f.read() #Leitura do Arquivo
    f = f.split("\n") #cria lista de evento por linha do arquivo
    graph = []
    for i in f[:-1]:
        dupla = i.split(",")
        graph.append((dupla[0],dupla[1]))
    return graph

def procura_aresta(list, no):
    count = 0
    for i in list:
        intersec = set(no[0]).intersection(set(i[1]))
        count += 1
        if intersec != set():
            return True,count
    return False, count


def tabusearch(g, btMax):
    iter = 0
    best_iter = 0
    vertex = []

    for v in g:
        vertex.append([[v,g.neighbors(v)]])

    cores = len(vertex)

    best_list = vertex[:]

    list_iter = vertex[:]

    while(iter - best_iter < btMax):

        cor1 = randint(0,cores-1)
        cor2 = randint(0,cores-1)
        no = randint(0,len(list_iter[cor1])-1)

        aux_no = list_iter[cor1][no]

        aresta, count = procura_aresta(list_iter[cor2], aux_no)

        if aresta == False:
            del(list_iter[cor1][no])
            list_iter[cor2].append(aux_no)
            try:
                list_iter.remove([])
            except :
                pass

            if len(list_iter) < len(best_list):
                best_iter = iter
                best_list = list_iter[:]
                cores = len(list_iter)
        iter += count

    return cores , iter
        



input = sys.argv[1:][0]
data = my_read(input)
g = Graph()
g.add_edges(data)
cores,i = tabusearch(g,100)
for k in range(0,50):
    new_cores , new_i = tabusearch(g,100)
    i += new_i
    if cores > new_cores:
        cores = new_cores
print(cores,":",i)