

class FormaGeometrica():

    #Dados
    base = 0
    altura = 0
    tipo = "R" # Retangulo

    def __init__(self, base = 0, altura = 0, tipo = "R"):
        self.base = base
        self.altura = altura
        self.tipo = tipo

retangulo1 = FormaGeometrica(15, 10, "R")

print(f"[retangulo1] base: {retangulo1.base}, altura: {retangulo1.altura}, tipo: {retangulo1.tipo}")