#importar valor da constante pi
from math import pi


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

def area_forma(base, altura, forma):
    """
    Função que calcula a área de uma das seguintes formas geométricas: retângulo, triângulo ou elipse Parametro forma: "R" == retangulo "T" == triângulo "E" == elipse
    """

    area = 0
    if forma == "R": #Retângulo
        area = base * altura
    elif forma == "T": #Triângulo 
        area = base * altura / 2 
    elif forma == "E": #Elipse
        area = (base / 2) * (altura / 2) * pi
    return area


print(f"Retângulo 7.5x11: {area_forma(7.5, 11, 'R')}")
print(f"Triângulo 8x12: {area_forma(8, 12,'T')}")
print(f"Circulo 15x15: {area_forma(15,15, 'E')}")