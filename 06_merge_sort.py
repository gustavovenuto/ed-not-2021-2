#   ALGORITMO DE ORDENAÇÃO MERGE SORT#
# No processo de ordenação, esse algoritmo "desmonta" o vetor original
# contendo N elementos até obter N vetores de apenas um elemento cada um.
# Em seguida, usando a técnica de mesclagem (merge), "remonta" o vetor,
# dessa vez com os elementos já em ordem.
    
def merge_sort(lista):
    """
        Função que implementa o algoritimo merge sort usando o método RECURSIVO
    """

    # Só continua se a lista tiver mais de um elemento
    if len(lista) > 1:
        meio = len(lista) // 2

        # Gerar cópia da primeira metade da lista
        lista_esq = lista[:meio] # Do inicio ao meio -1

        # Gera cópia da segunda metade da lista
        lista_dir = lista[meio:] # Do meio até o final


        # Chamamos recursivamente a função para continuar
        # repartindo a lista em metades
        lista_esq = merge_sort(lista_esq)
        lista_dir = merge_sort(lista_dir)

        # Junta as duas metades em uma unica lista, ordenada
        pos_esq = 0
        pos_dir = 0
        ordenada = []

        while pos_esq < len(lista_esq) and pos_dir < len(lista_dir):
            if lista_esq[pos_esq] < lista_dir[pos_dir]:
                ordenada.append(lista_esq[pos_esq])
                pos_esq += 1
            else: 
                ordenada.append(lista_dir[pos_dir])
                pos_dir += 1

    sobra = None # A sobra da lista que ficou para trás

    if(pos_esq < pos_dir):
        sobra = lista_esq[pos_esq:] #sobra da pos_dir até o final
    else: #houve sobra a direira
        sobra = lista_dir[pos_dir:] # Sobra do pos_dir até o final

    #Retornamos a lista ordenada, composta da ordenada _ sobra
    return ordenada + sobra # "Soma" de duas listas 

    ##################################################

nums = [88, 44, 33,0, 99, 55, 77, 22, 11, 66]

##nums_ord = merge_sort(nums)
##print(nums_ord)        


##################################################

from time import time
from data.nomes_desord import nomes
import tracemalloc

ini = time()
nomes_ord = merge_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

print(nomes_ord)
print(f"Tempo: {fim - ini}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")

tracemalloc.stop() #finaliza a medição do consumo de memória