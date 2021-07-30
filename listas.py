primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#percorrer a lista

print(primos)

for num in primos:
    print(num)

#acrescentar um novo elemento no fim da lista append()
primos.append(31)

print(primos)

#inserindo um elemento em uma posição especifica: insert()
primos.insert(0, 1)
print(primos)


#inserindo o 37 na posição 5
primos.insert(5, 37)
print(primos)

#retirando o ultimo elemento da lista: pop()
ultimo = primos.pop()
print(f'Removido o ultimo numero que é o: {ultimo}')
print(primos)

#removendo pelo valor: remove()
primos.remove(37)
print(primos)

#removendo por posição: del
#removendo o elemento da posição 4
del primos[4]
print(primos)

#fatiando uma lista
#exibindo apenas do elemento da posição 0 (inclusive) a posição 7 (exclusive)
print(primos[0:7])

#exibindoda posição 2 a posição 8
print(primos[2:8])

#fatiando e criando uma sublista
sub_primos = primos[1:5]
print(sub_primos)