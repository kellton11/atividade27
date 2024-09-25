# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

lista = []

# Solicite ao usuário que insira o nome de até 7 convidados.

for c in range (7):
    nome = input("digite o nome de até 7 convidado: ")
    lista.append(nome)
    len(lista)

r = input("deseja remover alguém (sim/não)?")


if r =="sim":
    n = input("nome do convidado: ")
    lista.remove(n)

else:
    print(lista)

print(lista)
