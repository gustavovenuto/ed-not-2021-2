# Dicionário é uma estrutura da linguagem python
# Capaz de armazenar multiplos valores em uma unica
# Variavel, por meio de pares de chave-valor
pessoa = {
    #"nome" é a chave
    # "fulano de tal é o valor"
    "nome": "Fulano de tal",
    "sexo": "M",
    "idade": 39,
    "peso": 76,
    "altura": 1.82
}

# Calculando o imc (Indice de massa corporal)
imc = pessoa["peso"] / (pessoa["altura"] ** 2)
print(f"O IMC de {pessoa['nome']} é {imc}.")

formal = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" # Retangulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T" # triangulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E" #elipse
}


def calcular_area(form):
    if forma["tipo"] == "R":
        return forma["base"] * forma["altura"]
        elif forma["tipo"] == "T":
            return forma["base"] * forma["altura"] / 2
        elif forma["tipo"] == "E": 
            return forma["base"] / 2 * forma["altura"] / 2 * pi
        else:
            #gera um erro
            raise Exception("Tipo de forma não reconhecida")
print(f"Area de um retangulo de 7.5x12: {calcular_area(forma1)}")
print(f"Area de um Triangulo de 6x2.5: {calcular_area(forma2)}")
print(f"Area de um retangulo de 5x3W: {calcular_area(forma3)}")

}