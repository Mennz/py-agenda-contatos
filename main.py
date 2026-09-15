from agenda import (
    adicionar_contato,
    listar_contatos,
    buscar_contato,
    remover_contato,
    salvar_contatos,
    carregar_contatos,
)

contatos = carregar_contatos()


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
            salvar_contatos(contatos)
            print("contato adicionado")
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            nome = input("Nome para buscar: ")
            encontrados = buscar_contato(contatos, nome)
            if not encontrados:
                print("nenhum contato encontrado")
            else:
                for contato in encontrados:
                    print(f"{contato['nome']} - {contato['telefone']}")
        elif opcao == "4":
            nome = input("Nome para remover: ")
            if remover_contato(contatos, nome):
                salvar_contatos(contatos)
                print("contato removido")
            else:
                print("contato nao encontrado")
        elif opcao == "5":
            print("ate mais!")
            break
        else:
            print("opcao invalida")


if __name__ == "__main__":
    main()
