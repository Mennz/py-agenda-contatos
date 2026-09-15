from agenda import adicionar_contato

contatos = []


def mostrar_menu():
    print("\n--- Agenda de Contatos ---")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar por nome")
    print("4 - Remover contato")
    print("5 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            adicionar_contato(contatos, nome, telefone)
            print("contato adicionado")
        elif opcao == "2":
            print("listar ainda nao foi feito")
        elif opcao == "3":
            print("buscar ainda nao foi feito")
        elif opcao == "4":
            print("remover ainda nao foi feito")
        elif opcao == "5":
            print("ate mais!")
            break
        else:
            print("opcao invalida")


if __name__ == "__main__":
    main()
