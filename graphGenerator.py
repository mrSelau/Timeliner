import sys
import numpy as np
####################################################################
# Rodar:
# python3 geradorGrafo.py <arquivo>
###################################################################
def main(data):
	eventos = read_time_line(data) # lê txt e cria lista de eventos ordenados decrescentemente
	text = geraGrafo(eventos)

def read_time_line(data):#leitura e tratamento da entrada txt
	f = open(data, 'r')
	f = f.read() #Leitura do Arquivo
	f = f.split("\n") #cria lista de evento por linha do arquivo
	
	list_event = []
	for i in f:
		x = i.split(",") #cada evento vira uma lista: [nome,inicio,fim]
		ix = np.arange(int(x[1]),int(x[2])+1,1)
		print(ix)
		list_event = list_event + [ix] #insere um evento na lista de eventos
	return list_event

def geraGrafo(list_event):
	grafo = ""
	count = 0
	text = ""
	for x in range(0,len(list_event)):
		first = list_event[x][0]
		last = list_event[x][-1]

		for y in range(x+1,len(list_event)):
			intersec = set(list_event[x]).intersection(list_event[y])

			if (intersec != set()) and (intersec != {first}) and (intersec != {last}):
				count += 1
				text += "("+str(x)+","+str(y)+")"+","+"\n"
	arquivo.write(text)

data = sys.argv[1:][0]
arquivo = open("grafo"+data, 'w')
main(data)
