
frutas=["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

#imprimindo apenas a fruta "uva"
print(frutas[2])

#substituição "pera" por "melão"
frutas[3] = "melão"
print(frutas)

#descobrindo quantos tem a lista
print(len(frutas))

#percorrendo e imprimindo cada um dos elementos da lista
for lista in frutas:
    print(lista)

#percorrendo e imprimindo cada elemento e sua posição
for i in range(len(frutas)):
    print(f"{frutas[i]} está na posição {i}")


#percurso em ordem invertida
#1 argumento: len(frutas) -1: a lista precisa começar no ultimo elemento, que é determinado por len() -1
#2 argumento: -1 porque o limite final não entra e precisamos terminar em 0
#3 argumento: -1, porque a lista precisa ser decrecente
for j in range(len(frutas)-1, -1, -1):
    print(frutas[j])

print('----------------------------------')

#ordenando o vetor em ordem alfabética
frutas.sort()
print(frutas)
