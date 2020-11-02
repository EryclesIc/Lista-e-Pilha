from linkedlist import LinkedList
from pilha import Stack
import csv
import random
import ctypes

csv.field_size_limit(int(ctypes.c_ulong(-1).value // 2))
lista = LinkedList()
stack = Stack()

def menu_listas():
    print("Olá, escolha qual estrutura deseja utilizar:")
    print("1- Lista encadeada")
    print("2- Pilha")
    escolha = int(input())

    if escolha == 1:
        print("Tudo bem, qual operação você deseja?")
        print("1- Inserir um novo elemento")
        print("2- Visualizar lista")
        print("3- Apagar um elemento da lista")
        print("4- Editar um elemento da lista")
        escolha = int(input())
        if escolha == 1:
            novo_elem(1)
        elif escolha == 2:
            visualizar_lista(1)
        elif escolha == 3:
            apagar_elem(1)
        elif escolha == 4:
            editar_elem(1)
    
    elif escolha == 2:
        print("Tudo bem, qual operação você deseja?")
        print("1- Inserir um novo elemento")
        print("2- Visualizar o topo da pilha")
        print("3- Deletar o topo da pilha")
        print("4- Editar topo da pilha")
        escolha = int(input())
        if escolha == 1:
            novo_elem(2)
        elif escolha == 2:
            visualizar_lista(2)
        elif escolha == 3:
            apagar_elem(2)
        elif escolha == 4:
            editar_elem(2)

def novo_elem(estrutura):
    print("Digite o elemento que deseja adicionar:")
    elemento = input()
    if estrutura == 1:
        lista.append(elemento)
        print("O {} foi adicionado a lista".format(elemento))
        print("A lista agora tem o tamanho {}.".format(len(lista)))
        print("Deseja adicionar outro elemento?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            novo_elem(1)
        elif escolha == 2:
            menu_listas()
    
    elif estrutura == 2:
        stack.push(elemento)
        print("O {} foi adicionado a pilha".format(elemento))
        print("A pilha agora tem o tamanho {}.".format(stack._size))
        print("Deseja adicionar outro elemento?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            novo_elem(2)
        elif escolha == 2:
            menu_listas()

def visualizar_lista(estrutura):
    if estrutura == 1:
        print(lista)
        print("A lista agora tem o tamanho {}.".format(len(lista)))
        print("Deseja visualizar a lista novamente?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            visualizar_lista(1)
        elif escolha == 2:
            menu_listas()
    
    elif estrutura == 2:
        print(stack)
        print("A pilha agora tem o tamanho {}.".format(stack._size))
        print("Deseja visualizar a pilha novamente?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            visualizar_lista(2)
        elif escolha == 2:
            menu_listas()

def apagar_elem(estrutura):
    if estrutura == 1:
        print(lista)
        print("Digite o elemento que deseja apagar:")
        elemento = input()
        lista.remove(elemento)
        print("O {} foi apagado da lista".format(elemento))
        print("A lista agora tem o tamanho {}.".format(len(lista)))
        print("Deseja apagar outro elemento?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            apagar_elem(1)
        elif escolha == 2:
            menu_listas()
    
    elif estrutura == 2:
        print(stack)
        print("Somente o topo da pilha pode ser removido.\nTem certeza que deseja continuar?")
        print("1- Sim")
        print("2- Não")
        decidir = int(input())
        if decidir == 1:
            elemento = stack.peek()
            stack.pop()
            print("O {} foi apagado do topo pilha".format(elemento))
            print("A pilha agora tem o tamanho {}.".format(stack._size))
            print("Deseja apagar outro elemento?")
            print("1- Sim")
            print("2- Não. Voltar para o menu principal")
            escolha = int(input())
            if escolha == 1:
                apagar_elem(2)
            elif escolha == 2:
                menu_listas()
        elif decidir == 2:
            menu_listas()

def editar_elem(estrutura):
    if estrutura == 1:
        print(lista)
        print("Digite o elemento que deseja editar:")
        elemento = input()
        endereco = lista.index(elemento)
        
        print("Digite o novo elemento:")
        lista[endereco] = input()
        
        print("O {} foi editado na lista para {}".format(elemento, lista[endereco]))
        print("A lista agora tem o tamanho {}.".format(len(lista)))
        print("Deseja editar outro elemento?")
        print("1- Sim")
        print("2- Não. Voltar para o menu principal")
        escolha = int(input())
        if escolha == 1:
            editar_elem(1)
        elif escolha == 2:
            menu_listas()
    
    elif estrutura == 2:
        print(stack)
        print("Somente o topo da pilha pode ser editado.\nTem certeza que deseja continuar?")
        print("1- Sim")
        print("2- Não")
        decidir = int(input())
        if decidir == 1:
            elemento = stack.peek()
            stack.pop()
            print("Digite o elemento novo:")
            edit = input()
            stack.push(edit)
            print("O {} foi editado do topo pilha para {}".format(elemento, edit))
            print("A pilha agora tem o tamanho {}.".format(stack._size))
            print("Deseja editar outro elemento?")
            print("1- Sim")
            print("2- Não. Voltar para o menu principal")
            escolha = int(input())
            if escolha == 1:
                editar_elem(2)
            elif escolha == 2:
                menu_listas()
        elif decidir == 2:
            menu_listas()

with open('metadata.csv', encoding="utf-8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter='\n')

    numero_coluna = 0
    i = 0
    row1 = next(csv_reader)
    numero_coluna = len(row1[0].split(","))

    for row in csv_reader:
        i = i + 1
    numero_de_linhas = i

    data = ""
    for i in range(100):
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
                stack.push(data)
            x = x + 1
    print("\n")
menu_listas()