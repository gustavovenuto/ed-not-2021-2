# FATORIAL DE UM NUMERO N
# É IGUAL AO NUMERO N MULTIPLICADO POR TODOS OS SEUS ANTECESSORES ATÉ 1

# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 (5040)


# 5! = 5 * 4 * 3 * 2 * 1 (120)
# 4! = 4 * 3 * 2 * 1 (24)
# 3! = 3 * 2 * 1 (6)
# 2! = 2 * 1 (2)
# 1! = 1
# 0! = 1 (por convenção)


# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 * 0!

#n! = n* (n-1)! p/ n>1


def fatorial(n):
    resultado = 1
    if(n > 1):
        # range começa no numero n e vai descendo até 1
        for i in range(n, 1, -1):
            resultado *= 1
            print(f'Resultado: {resultado}, i: {i}')
    return resultado 

print(f'5! = {fatorial(5)}') 
print(f'7! = {fatorial(5)}')

# n! = n * (n - 1)! p/n > 1
# Recursividade ocorre quando a definição de uma função inclui a própria
# função sendo definida

# Em programação, a recursividade se traduz quando uma função efetua
# chamadas a si própria.

def fatorial2(n):
    if n <= 1:
        return 1
    return n * fatorial2(n - 1)
