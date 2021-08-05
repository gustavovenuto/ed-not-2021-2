#função é um trecho de código que tem um nome e pode receber informações
#externas para fazer seu trabalho.
#Opcionalmente, uma função pode tambem produzir um valor de resultado

#uma função é definida apenas uma vez e pode ser utilizada
#(chamada) várias vezes, evitando repetições de código.
#existem funções já providas(prontas) pela linguagem, como, por exemplo
#len(), range() e sort(), e podemos definir tambem nossas próprias funções.

#a função imc() está esperando o valor desses 2 parametros peso e altura
def imc(peso, altura): #definição (ou declaração da função)
    #trechos com aspas triplas são um tipo especial de comentário chamado docstring, e servem para documentas o propósito de uma função ou classe.
    """
        É uma função que calcula o indice de massa corpórea (IMC) 
    """
    return peso / altura **2 #peso / altura ao quadrado

#float() converte o valor informado em um numero com casas decimais
p = float(input('Informe o peso da pessoa:'))
a = float(input('Informe a altura da pessoa:'))

#fazendo uma chamada a função imc() e passando os valores como parametro
resultado = imc(p, a) #passando o valor de a e b como parametro para a função imc e recebendo o resultado

print(f"O IMC calculado é {resultado}.")