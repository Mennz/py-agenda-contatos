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


def buscar_contato(contatos, nome):
    nome = nome.lower()
    encontrados = [c for c in contatos if nome in c["nome"].lower()]
    return encontrados
