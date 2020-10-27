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
	for i in list:
		intersec = set(no[0]).intersection(set(i[1]))
		if intersec != set():
			return True
	return False


def tabusearch(g, btMax):
    iter = 0 #contador
    best_iter = 0
    vertex = []

    for v in g:
        vertex.append([[v,g.neighbors(v)]])

    cores = len(vertex)

    best_list = vertex[:]

    while(iter - best_iter < btMax):
    	aux_list = vertex [:]
    	iter += 1

    	cor1 = randint(0,cores-1)
    	cor2 = randint(0,cores-1)
    	no = randint(0,len(vertex[cor1])-1)

    	aux_no = vertex[cor1][no]

    	aresta = procura_aresta(aux_list[cor2], aux_no)

    	if aresta == False:
    		del(aux_list[cor1][no])
    		aux_list[cor2].append(aux_no)
    		try:
    			aux_list.remove([])
    		except :
    			pass

    		if len(aux_list) < len(vertex):
    			best_iter = iter
    			vertex = aux_list
    			cores = len(vertex)
    print(cores ,":", iter)
    	



input = sys.argv[1:][0]
data = my_read(input)
g = Graph()
g.add_edges(data)
tabusearch(g,10)









