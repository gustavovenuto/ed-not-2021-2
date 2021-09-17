from lib.stack import stack

# Criando uma pilha

pilha = stack()
print(pilha.to_str())


# Empilhando alguns valores
pilha.push(10)
pilha.push(13)
pilha.push(19)
pilha.push(23)
pilha.push(27)
pilha.push(33)

print(pilha.to_str())

# Retira um elemento da pilha
removido = pilha.pop()
print(f"Removido: {removido}, pilha: {pilha.to_str()}")

while not pilha.is_empty():
    print(pilha.pop())