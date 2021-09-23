"""
    ANALIZSADOR DE EXPRESSOES MATEMATICAS
"""

from lib.stack import stack

simbolos = {
    "P": "parentese",
    "C": "colchete",
    "X": "chave"
}

expressao = "2 * 4 - {7 / [5 -(7 * 9) + 1] * 3} / 5"

analisador = stack() # Cria a pilha

def verif_fechamento(tipo_fecha, pos_fecha, dados_abre):
    #if dados["tipo"] == tipo:
    #   print(f"Simbolo {tipo} aberto na posição {dados['pos']} e fechado na posição {pos}") 

    if dados_abre is None:
        print(f"ERRO: há mais simbolos de fechamento que simbolos de abertura na expressão; topo {tipo_fecha}, posição {pos_fecha}")
    elif dados_abre["tipo"] == tipo_fecha:
        print(f"Simbolo tipo {tipo_fecha} aberto na posição {dados_abre['pos']} e fechamento na posição {pos_fecha}")

# Percorre a expressão em busca de parênteses, colchetes e chaves
for pos in range(len(expressao)):
    if expressao[pos] == "(":
        # Empilha informações sobre o abre parênteses
        analisador.push({ "tipo": "P", "pos": pos})
    elif expressao[pos] == "[":
        # Empilha informações sobre o abre colchetes
        analisador.push({ "tipo": "C", "pos": pos})
    elif expressao[pos] == "{":
        # Empilha informações sobre o abre chaves
        analisador.push({"tipo": "X", "pos": pos})
    elif expressao[pos] == ")":
        verif_fechamento("P", pos, analisador.pop())
    elif expressao[pos] == "]":
        verif_fechamento("C", pos, analisador.pop())
    elif expressao[pos] == "}":
        verif_fechamento("X", pos, analisador.pop())

# Verificando se houve sobra(s) na pilha

while not ana

print(analisador.to_str())