import sys
from random import randint
####################################################################
# Rodar:
# python3 gerador.py <quantidade_timelines> <quantidade maxima de eventos> <ano_inicio> <ano_final> "<nome>"
###################################################################
def gerador_without_gap(num_timelines, num_max_events, init, end, name): #gerador sem tamanho max de evento
	
	timelines_decreasing = open("decreasing/timelinesdecreasing.sh", 'w') # txt com o nome de todas timelines
	timelines_growing = open("growing/timelinesgrowing.sh", 'w') # txt com o nome de todas timelines
	text = "" # texto a ser colocado em timelines.txt
	for n in range(1 , num_timelines+1):
		num_events_timeline_current =  int((n * num_max_events) / num_timelines) # quantidade de eventos da timeline da iteração
		name_timeline_current =  str(n) + name + "_"+ str(num_events_timeline_current) + "events.txt" # nome da timeline no .txt
		timeline_current = open(name_timeline_current, 'w')
		x = "" # texto da timeline atual
		for i in range(1, num_events_timeline_current+1):
			first = randint(init,end-1) #sorteia data inicial
			last = randint(first+1,end) #sorteia data final
			x +='\n'+','+str(first)+','+str(last)
		timeline_current.write(x[1:])
		text +='\n'+ "python3 timeliner.py ../" +name_timeline_current
	timelines_decreasing.write(text[1:])
	timelines_growing.write(text[1:])


##################################################################
num_timelines  = int(sys.argv[1:][0]) #quantidade maxima de eventos
num_max_events = int(sys.argv[1:][1]) #quantidade maxima de eventos
init           = int(sys.argv[1:][2]) #data do inicio mais antigo
end            = int(sys.argv[1:][3]) #data do final mais recente
name           = sys.argv[1:][4]

gerador_without_gap(num_timelines, num_max_events, init, end, name)

