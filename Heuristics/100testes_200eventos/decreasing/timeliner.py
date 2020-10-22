# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
import sys
####################################################################
# Rodar:
# python3 timelinemaker.py <entrada.txt> 
####################################################################
def main(data):
	eventos,first,last = read_time_line(data) # lê txt e cria lista de eventos ordenados decrescentemente
	plot_config(first,last,data[0:-4]) # configura gráfico com medidas
	inicio = time.time() # tempo de inicio do programa
	lines, intersection = organize_timeline(eventos) # distribui eventos na menor quantidade de linhas
	fim = time.time() # tempo do fim do programa
	print(len(lines),":",intersection,":",fim - inicio)
	img = data[:-4]+".png"
	#plt.savefig(img, transparent = True) # salva figura
	#print("Tempo: ",fim - inicio) # printa duração do programa
	#plt.show()

def read_time_line(data):#leitura e tratamento da entrada txt
	f = open(data, 'r')
	f = f.read() #Leitura do Arquivo
	f = f.split("\n") #cria lista de evento por linha do arquivo
	first = 9999 
	last = 0000
	list_event = []
	for i in f:
		x = i.split(",") #cada evento vira uma lista: [nome,inicio,fim]
		x.append((int(x[2])-int(x[1]))) #insere a duração do evento: [nome,inicio,fim,duraçao]
		list_event = list_event + [x] #insere um evento na lista de eventos
		if int(x[1]) < first:
			first = int(x[1]) # guarda a data de inicio do evento mais antigo
		if int(x[2]) > last:
			last = int(x[2]) # guarda a data de fim do evento que termina por ultimo
	list_event.sort(key=lambda x: x[3], reverse = True) #ordena lista de eventos pela duração maior->menor
	return list_event,first,last

def organize_timeline(events):# distribui eventos na menor quantidade de linhas
	list_line = [] #cada lista será uma linha no gráfico(lista de listas)
	intersection_aux = 0
	intersection = 0
	for i in events: #para cada eventos
		if list_line == []:
			list_line = [[i]] #cria a primeira linha, com o primeiro o evento
		else:
			for j in list_line: # para cada linha
				verify, intersection_aux = verify_intersection(j,i) # verifica se o evento tem intersecção com outro evento da linha
				intersection += intersection_aux
				if verify == False: # se não tem intersecção
					j.append(i) # coloca evento na linha
					break # não é necessário verificar para outras linhas
			if verify == True:# se houve intersecção em todas linhas 
				list_line.append([i])# adiciona nova linha
	my_plot(list_line) # chama função que monta o gráfico com os eventos
	return list_line, intersection

def verify_intersection(list,var):
	verify = False
	var_list = np.arange(int(var[1]),int(var[2])+1,1)
	first = var_list[0]
	last = var_list[len(var_list)-1]
	teste = []
	intersection = 0
	for i in list:
		intersection += 1
		aux =np.arange(int(i[1]),int(i[2])+1,1)
		teste = i[0]
		x = set(var_list).intersection(aux)
		if (x != set()) and (x != {first}) and (x != {last}):
			verify = True
			break
	return verify, intersection

def my_plot(list):
	num = 1
	for i in list:
		for j in i:
			length = np.arange(int(j[1]),int(j[2])+1,1)
			my_plot_uni(j,length,num)
		if num>0:
			num = num * (-1)
		else:
			num = (num * (-1)) + 1

def my_plot_uni(i, length, line):
	x = (int(i[1]) + int(i[2]))/2 - 0.45
	plt.plot(length,((length/length)*line),label=i[0],linewidth=10)
	plt.annotate(i[0], xy=(x,line+0.2))

def timeline(x):
	t = 0
	while(t<len(x)):
		plt.plot(x[t], x[t]*0, linestyle='', color='black', marker='o')
		plt.annotate(str(x[t]), xy=(x[t]-0.16,0+0.3))
		t = t+1

def plot_config(first,last,name):
	plt.style.use('seaborn')
	plt.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)
	plt.title(name)
	plt.xlabel('Time')
	plt.ylabel('Event')
	timeline(np.arange(first,last+1,1))


data = sys.argv[1:][0]
main(data)

