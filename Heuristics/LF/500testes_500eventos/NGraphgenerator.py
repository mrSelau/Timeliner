import os
import sys
import numpy as np

def main(data, diretorio):
	eventos = read_time_line(diretorio+"/"+data) # lê txt e cria lista de eventos ordenados decrescentemente
	text = geraGrafo(eventos)
	return text

def read_time_line(data):#leitura e tratamento da entrada txt
	f = open(data, 'r')
	f = f.read() #Leitura do Arquivo
	f = f.split("\n") #cria lista de evento por linha do arquivo
	
	list_event = []
	for i in f:
		x = i.split(",") #cada evento vira uma lista: [nome,inicio,fim]
		ix = np.arange(int(x[1]),int(x[2])+1,1)
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
				text += str(x)+","+str(y)+"\n"
	return text

#############################################################################################
diretorio = "/home/mrselau/Documentos/Timeliner/Timeliner/Heuristics/500testes_500eventos"

timelines = [timeline for timeline in os.listdir(diretorio) if timeline.endswith('.txt')] #lista de timelines em um txt

aux = []
for i in timelines:
	t = i.replace("teste_","_")
	j = t.replace("events.txt","")
	j = j.split("_")
	aux.append((int(j[0]),i))

aux.sort()

execute = open("graph.sh", 'w') # txt com o nome de todas timelines
text = "" # texto a ser colocado em timelines.txt
for i in aux:
	arquivo = open("grafo"+i[1], 'w')
	graph = main(i[1],diretorio)
	arquivo.write(graph)
	text +='\n'+ "sage LF.sagews grafo" +i[1]
	arquivo.close()
execute.write(text[1:])