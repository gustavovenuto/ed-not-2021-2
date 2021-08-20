# ALGORITIMO DE ORDENAÇÃO SELECTION SORT

# Isola (seleciona) o primeiro elemento da lista e, em seguida, encontra
# encontra o menor valor no restante da lista. Se o valor encontrado for menor que o valor selecionado, efetua a troca.
# Em seguida, isola o segundo número da lista, buscando pelo menor
# valor da posições subsequentes, faz a troca entre os dois valores,
# se necessario. continua o processo, até isolar o penúltimo elemento
# da lista.


comps = 0 
passadas = 0
trocas = 0


def selection_sort(lista):
    """
        Função que implementa o algoritimo de ordenação selection sort
    """

    global comps, passadas, trocas

    comps = 0
    passadas = 0
    trocas = 0


    # Percurso da lista até a penultima posição
    for i in range(len(lista)-1):
        #print(lista[i])
        #print('fim i')
        passadas += 1
        # Seleciona (isola) o elemento que será comparado
        pos_sel = i

        # Rotina para encontrar o menor do resto da lista
        pos_menor = i + 1

        # Percurso da lista da posição i+2 até o fim
        for j in range(i + 2, len(lista)):
            #print(lista[j])
            #print('fim j')
            comps += 1
            # Se o elemento da posição atual (j) for menor
            # que o elemento na posição do menor(pos_menor)
            # atualizamos pos_menor
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        comps += 1
        # Comparamos lista[sel] com lista[pos_menor] e, se segundo
        # for menor que o primeiro, efetuamos a troca entre eles
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor] 
            trocas += 1
            #print('troca')

###############################################################################

# Valores da variaveis no inicio do selection sort
# pos_sel: 0 (onde está o 88)
# pos_menor: 1(onde está o 44)
# j:2(onde está o 33)
#nums = [88, 44, 33, 0, 99, 55, 77, 22, 11, 66]

# pior caso - 
nums = [99, 88, 77, 66, 55, 44, 33, 22, 11, 0]

# melhor caso - nums = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

selection_sort(nums)
print(nums)
print(f"Comparações: {comps}")
print(f"Passadas: {passadas}")
print(f"Trocas: {trocas}")


from time import time
from data.nomes_desord import nomes


#nomes_parcial = nomes[:50000] # usa apenas os primeiros 20 mil nomes

ini = time()
#selection_sort(nomes_parcial)
selection_sort(nomes)
fim = time()

#print(nomes_parcial)
print(nomes)
print(f"Tempo: { fim - ini}")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")