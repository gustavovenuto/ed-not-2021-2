#   ALGORITMO DE ORDENAÇÃO QUICK SORT
#   Escolhe um dos elementos do vetor para ser o pivô (na nossa implementação,
#   o último elemento) e, na primeira passada, divide o vetor, a partir da posição
#   final do vetor, em um subvetor à esquerda contendo apenas valores menores que
#   o pivô e outro subvetor à direita, que contém apenas valores maiores que o pivô.

#   Em seguida, recursivamente, repete o processo em cada uma das sublistas até que toda a #lista esteja ordenado.

passadas = 0
comps = 0
trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    """
        Função que implementa o algoritimo de ordenação Quick Sort
        de forma recursiva
    """

    # Se fim for None, então consideramos o ultima posição do vetor
    if fim is None:
        fim = len(lista)-1

    # Para continuarmos, precisamos que a lista tenha pelo menos
    # Dois elementos para ordernar
    if fim <= ini:
        return # Sai da função sem fazer nada

    global passadas, comps, trocas

    passadas += 1    

    pivot = fim
    div = ini -1 #D Divisor inicio antes do primeiro elemento

     # Percorre a lista da posição ini até a posição fim - 1    
    for i in range(ini, fim):
        comps += 1
        if lista[i] < lista[pivot]:
            div += 1    
            # Incrementa o divisor            
            # lista[div] e lista[i] trocam de lugar entre si,            
            # caso não sejam o mesmo elemento            
            if div != i:
                lista[div], lista[i] = lista[i], lista[div]
                trocas += 1
    # Depois que o percurso de i acaba, div ainda é incrementado    
    # mais uma vez    
    div += 1    
    # Colocamos o pivô em seu lugar definitivo. A troca acontece    
    # se o valor do pivô for menor que o valor da posição div 
    comps += 1   
    if lista[pivot] < lista[div] and pivot != div:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1
    # Chamamos recursivamente a função para a sublista à esquerda    
    # da posição div    
    quick_sort(lista, ini, div - 1)
    # Chamamos recursivamente a função para a sublista à direita    
    # da posição div    
    quick_sort(lista, div + 1, fim)
#####################################################################
nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]
quick_sort(nums)
print(nums)
print(f"Passadas: {passadas}, comps: {comps}, trocas: {trocas}")

from data.nomes_desord import nomes
from time import time
import tracemalloc

#nomes_parcial = nomes[:30000]   # Usa apenas os primeiros 30 mil nomes

ini = time()
#selection_sort(nomes_parcial)
quick_sort(nomes)

mem_atual, mem_pico = tracemalloc.get_traced_memory()

fim = time()

#print(nomes_parcial)
print(nomes)
print(f"Tempo: {fim - ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")

print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")