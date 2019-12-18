import math
# quantidade de blocos
# para cada arquivo:
# 	- o bloco inicial
#	- a quantidade de blocos necessária
def alocar(initial, qtd, memoria, arq):
	if memoria[initial] != "LIVRE":
		print("\n   BLOCOS DE MEMÓRIA LIVRE (0)")
		print(memoria_livre)
		return 1
	else:
		for j in range(qtd):
			try:
				if memoria[initial + j] != "LIVRE":
					return 1
			except:
				return 1
		for j in range(qtd):
			memoria[initial + j] = "Arquivo " + str(arq)
			memoria_livre[initial + j] = 1
		return 0

def alocar_encadeada(initial, qtd, memoria_encadeada, arq):
	if initial + 1 not in memoria_livre_encadeada:
		print("\n   BLOCOS DE MEMÓRIA LIVRE (0)")
		print(encadeada_uso_memoria)
		return 1
	else:
		for j in range(qtd):
			try:
				# localizar uma posição em memoria_livre_encadeada
				# preencher essa posição no vetor memoria_encadeada
				# adicionar na chave do arquivo no dicionário T
				if j == 0:	
					memoria_livre_encadeada.remove(initial + 1)
					memoria_encadeada[initial] = "Arquivo " + str(arq)
					encadeada_uso_memoria[initial] = 1
					T[arq].append(initial)
				else:
					new_pos = memoria_livre_encadeada.pop()
					memoria_encadeada[new_pos - 1] = "Arquivo " + str(arq)
					encadeada_uso_memoria[new_pos - 1] = 1
					T[arq].append(new_pos + 1)
			except:				
				return 1
		return 0


quadros = int(input("\tQuantidade de blocos de memória: "))
qtd = int(input("\tQuantidade de arquivos a serem armazenados: "))
tam = int(input("\tTamanho de cada bloco: "))

opt = int(input("\n\t(1) - Alocação contígua / (2) - Lista Encadeada: "))

memoria = []
memoria_encadeada = []
memoria_livre = []
memoria_livre_encadeada =[]
encadeada_uso_memoria = []

for i in range(quadros):
	memoria.append("LIVRE")
	memoria_livre.append(0)
	encadeada_uso_memoria.append(0)
	memoria_encadeada.append(0)
	memoria_livre_encadeada.append(i+1)

# armazena os blocos usados para cada arquivo - lista encadeada
T = dict()
for k in range(qtd):
	T[k+1] = []

print()

for i in range(qtd):
	keep = True
	while keep:
		print("Arquivo ", i + 1, end=" :\n")
		print("   Bloco inicial (",1, " à ", quadros, "): ", end="")
		bloco = int(input())
		tam_arquivo = int(input("   Tamanho do arquivo: "))

		qtd_bloco = math.ceil(tam_arquivo / tam)
		print("   Blocos necessários : ", qtd_bloco)

		result = 0
		if opt == 1:
			result = alocar(bloco - 1, qtd_bloco, memoria, i + 1)
		else:
			result = alocar_encadeada(bloco - 1, qtd_bloco, memoria_encadeada, i + 1)

		if result == 1:
			print("   WARNING: Arquivo não pode ser alocado com essa configuração, repita!")
			keep = True
		else: 
			print("   Alocado!\n")
			keep = False
print("\n\tBLOCOS DE MEMÓRIA")
if opt == 1:	
	print(memoria)

	print("\n\tBLOCOS DE MEMÓRIA LIVRE")
	print(memoria_livre)
else:
	print(memoria_encadeada)
	print("\n\tBLOCOS DE MEMÓRIA LIVRE")
	print(encadeada_uso_memoria)
