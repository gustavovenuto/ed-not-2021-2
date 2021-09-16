#Palindromo: é um texto que, quando lido de trás para frente, 
#mantem o mesmo contéudo(desprezando acentos e espaçamento)
#texto = "SOCORRAM-ME, SUBI NO ONIBUS EM MARROCOS"

texto = "BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHÃO"

pilha= []

# Percurso do palindromo, colocando cada letra na lista

for letra in range(len(texto)):
    pilha.append(texto[letra])

inverso = ""

# Retira cada çetra da lista, de trás para frente, e coloca no inverso

while len(pilha) > 0:
    inverso += pilha.pop() # pop() retira sempre o ultimo elemento

print(inverso)

# Pilha

# A pilha é um tipo abstrato de dados (TAD) que permite a entra e a saida
# de dados apenas na sua extremidade final. Como consequencia, ela segue a regra
# lifo (last in, first out - ultimo a entrar, primeiro a sair)