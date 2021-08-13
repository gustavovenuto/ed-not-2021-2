# ALGORITIMO DE ORDENAÇÃO BUBBLE SORT

# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menor que o primeiro.Efetua tantas passadas quanto necessárias
# até que na ultima passada, nenhuma troca seja efetuada


def bubble_sort(lista):
    """
        Função que implementa o algoritimo de ordenação Bubble Sort
    """

    while True: # Loop eterno
        trocou = False
        #Loop na lista até o penultimo elemento. Porque ele já compara com o ultimo
        #ex. em uma lista de 10 elementos, len(lista) == 10
        # A ultima posição estára em len(lista) -1, porcausa que começa a contar apartir de 0, ou seja len(lista) - 1 == 9
        #A penultima posição será len(lista) -2, ou seja 8
        
        for i in range(len(lista)-2): #inicia nova passada
            if lista[i + 1] < lista[i]: #necessario trocar
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
                trocou = True

        # Se ouve troca, a lista está ordenada e podemos interromper
        # O loop while
        if not trocou:
            break # Interrompe o while