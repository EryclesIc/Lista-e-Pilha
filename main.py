from linkedlist import LinkedList


def novo_elem():
    print("Digite o elemento que deseja adicionar:")
    elemento = input()
    lista.append(elemento)
    print("O {} foi adicionado a lista".format(lista[0]))
    print("A lista agora tem o tamanho {}.".format(len(lista)))
    print("Deseja adicionar outro elemento?")
    print("1- Sim")
    print("2- Não")
    escolha = int(input())
    if escolha == 1:
        novo_elem()
    else:
        pass


print("Olá, escolha qual estrutura deseja utilizar:")
print("1- Lista")
print("2- Pilha")
escolha = int(input())

if escolha == 1:
    print("Tudo bem, qual operação você deseja?")
    print("1- Inserir um novo elemento")
    print("2- Atualizar um elemento da lista")
    escolha = int(input())
    if escolha == 1:
        lista = LinkedList()
        novo_elem()
    else:
        pass
else:
    print("Você entrou na pilha!")
