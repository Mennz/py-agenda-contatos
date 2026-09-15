def adicionar_contato(contatos, nome, telefone):
    contato = {"nome": nome, "telefone": telefone}
    contatos.append(contato)
    return contato


def listar_contatos(contatos):
    if not contatos:
        print("nenhum contato cadastrado")
        return

    for contato in contatos:
        print(f"{contato['nome']} - {contato['telefone']}")
