import sys
from random import randint
####################################################################
# Rodar:
# python3 gerador.py <quantidade_eventos> <tamanho_maximo_evento> <ano_inicio> <ano_final> "<nome>"
###################################################################
def gerador_without_gap(count,init,end): #gerador sem tamanho max de evento
	x = ""
	for i in range(count):
		first = randint(init,end-1) #sorteia data inicial
		last = randint(first+1,end) #sorteia data final
		x +='\n'+','+str(first)+','+str(last)
	arquivo.write(x[1:])

def gerador_with_gap(count,gap,init,end): #gerador com tamanho max de evento
	x = ""
	for i in range(count):
		first = randint(init,end-1) #sorteia data inicial
		last = randint(first+1,first+gap) #sorteia data final
		x += '\n'+','+str(first)+','+str(last)
	arquivo.write(x[1:])
##################################################################
count = int(sys.argv[1:][0]) #quantidade de eventos
gap = int(sys.argv[1:][1]) #tamanho de um evento
init = int(sys.argv[1:][2]) #data do inicio mais antigo
end = int(sys.argv[1:][3]) #data do final mais recente
nome = sys.argv[1:][4]+ ".txt"

arquivo = open(nome, 'w')

if gap < 0: # não possui tamanho, logo o final do evento pode ser end 
	gerador_without_gap(count,init,end)
else: # possui tamanho, logo tera duração de gap
	gerador_with_gap(count,gap,init,end)

