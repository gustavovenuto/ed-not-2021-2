# ALGORITIMO DE ORDENAÇÃO BUBBLE SORT

# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menor que o primeiro.Efetua tantas passadas quanto necessárias
# até que na ultima passada, nenhuma troca seja efetuada

comps = 0
passadas = 0
trocas = 0


def bubble_sort(lista):
    """
        Função que implementa o algoritimo de ordenação Bubble Sort
    """

    global comps, passadas, trocas

    comps = 0
    passadas = 0
    trocas = 0

    while True:  # Loop eterno
        passadas += 1

        trocou = False
        # Loop na lista até o penultimo elemento. Porque ele já compara com o ultimo
        # ex. em uma lista de 10 elementos, len(lista) == 10
        # A ultima posição estára em len(lista) -1, porcausa que começa a contar apartir de 0, ou seja len(lista) - 1 == 9 -> range(len(lista))
        # A penultima posição será len(lista) -2, ou seja, 8 -> range(len(lista))

        for i in range(len(lista)-1):  # inicia nova passada
            comps += 1
            if lista[i + 1] < lista[i]:  # necessario trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
                trocas += 1
                trocou = True

        # Se ouve troca, a lista está ordenada e podemos interromper
        # O loop while
        if not trocou:
            break  # Interrompe o while

# nums = [ 88, 44, 33, 0, 99, 55, 77, 22, 11, 66]


# pior caso - nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]

# melhor caso
nums = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

bubble_sort(nums)

print(nums)
print(f"Comparações: {comps}")
print(f"Passadas: {passadas}")
print(f"Trocas: {trocas}")



#-----------------------------------------------------#


from time import time
from data.nomes_desord import nomes


nomes_parcial = nomes[:30000] # usa apenas os primeiros 20 mil nomes

ini = time()
bubble_sort(nomes_parcial)
fim = time()

print(nomes_parcial)
print(f"Tempo: { fim - ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")