#print() usado para exibir informações
print("Olá Mundo !")

#input() usado para inserir informação
nome = input('Qual é o seu nome ?')

print(f'Olá {nome}')

#int() converte a string do input para numero inteiro
idade = int(input('Informe sua idade: '))

if idade >= 18: 
    print('Você já pode beber.')
    print('Você já pode tirar habilitação.')
else: 
    print('Você não pode beber')
    print('Você não pode tirar habilitação.')