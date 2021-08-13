#Algoritimo de busca binaria

#Dada uma lista, que deve estar previamente ordenada, e um valor de
#busca, divide a lista em duas metades e procura pelo valor de busca
#apenas na metade onde o valor poderia estar. Novas subdivisões são
#feitas até que se encontre o valor de busca ou que reste apenas uma
#sublista vazia, quando se conclui que o valor de busca não existe na
#lista.

from time import time
from data.lista_nomes import nomes

comps = 0

def busca_binaria(lista, valor_busca):
    """
        Função que implementa o algoritimo de busca sequencial

        Retorna a posição onde valor_busca foi encontrado
        O valor converncional -1 se valor_busca não existir na lista
    """
    global comps #Indica que estamos usando a variavel global declarada na linha 13
    comps = 0

    ini = 0  #primeira posição
    fim = len(lista) -1 #ultima posição

    while ini <= fim:
        meio = (ini + fim) // 2  #operador // é divisão inteira

        #1 caso: lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca:
            comps += 1
            return meio #meio é a posição onde o valor_busca está na lista
        #2 caso: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            comps += 2
            fim = meio -1 #descarta a 2 metade da lista

        #3 caso: valor_busca é maior que lista[meio]
        else:
            comps += 2
            ini = meio + 1 #descarta a 1 metade da lista
    #4 caso: valor_busca não encontrado na lista
    return -1  

comps = 0
hora_ini = time()
print(f"Posição do nome Orkutilson: {busca_binaria(nomes, 'ORKUTILSON')},{comps} comparações")
hora_fim = time()

print(f"Tempo gasto procurando Orkutilson: {(hora_fim - hora_ini) * 1000}ms")

comps = 0
hora_ini = time()
print(f"Posição do nome BELERINA: {busca_binaria(nomes, 'BELERINA')}, {comps} comparações" )
hora_fim = time()

print(f"Tempo gasto procurando BELERINA: {(hora_fim - hora_ini) * 1000}ms")

comps = 0
hora_ini = time()
print(f"Posição do nome AARAO: {busca_binaria(nomes, 'AARAO')}, {comps} comparações" )
hora_fim = time()

print(f"Tempo gasto procurando AARAO: {(hora_fim - hora_ini) * 1000}ms") 