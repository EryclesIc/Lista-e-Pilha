from linkedlist import LinkedList
from pilha import Stack
import csv
import random
import sys
csv.field_size_limit(sys.maxsize)
lista = LinkedList()
stack = Stack()


def novo_elem(estrutura):
    print("Digite o elemento que deseja adicionar:")
    elemento = input()
    if estrutura == 1:
        print(elemento)
        lista.append(elemento)
        print("O {} foi adicionado a lista".format(elemento))
        # print("o index desse elemento é {}".format(lista.index(elemento)))
        print("A lista agora tem o tamanho {}.".format(len(lista)))
        print("Deseja adicionar outro elemento?")
        print("1- Sim")
        print("2- Não")
        escolha = int(input())
        if escolha == 1:
            novo_elem(1)
        else:
            pass
    else:
        # print(elemento)
        stack.push(elemento)
        print("O {} foi adicionado a pilha".format(elemento))
        print("A pilha agora tem o tamanho {}.".format(stack._size))
        print("Deseja adicionar outro elemento?")
        print("1- Sim")
        print("2- Não")
        escolha = int(input())
        if escolha == 1:
            novo_elem(2)
        else:
            pass


with open('metadata.csv', encoding="utf-8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter='\n')

    # csv_reader.__next__()
    numero_coluna = 0
    i = 0
    row1 = next(csv_reader)
    numero_coluna = len(row1[0].split(","))

    for row in csv_reader:
        i = i+1
    numero_de_linhas = i

    data = ""
    for i in range(5):
        csv_file.seek(0)
        linha_sorteada = random.randint(0, numero_de_linhas)-1
        coluna_sorteada = random.randint(0, numero_coluna)-1

        x = 0
        for row in csv_reader:
            if x == linha_sorteada:
                data = row[0].split(",")[coluna_sorteada]
                print("***********************************")
                print(data)
                lista.append(data)
                break
            x = x+1
    print("\n")
    print("Olá, escolha qual estrutura deseja utilizar:")
    print("1- Lista encadeada")
    print("2- Pilha")
    escolha = int(input())

    if escolha == 1:
        print("Tudo bem, qual operação você deseja?")
        print("1- Inserir um novo elemento")
        print("2- Atualizar um elemento da lista")
        escolha = int(input())
        if escolha == 1:
            novo_elem(1)
        else:
            pass
    else:
        print("Tudo bem, qual operação você deseja?")
        print("1- Inserir um novo elemento")
        print("2- Visualizar o topo da pilha")
        print("3- Deletar o topo da pilha")
        escolha = int(input())
        if escolha == 1:
            novo_elem(2)
