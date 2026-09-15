def adicionar_contato(contatos, nome, telefone):
    contato = {"nome": nome, "telefone": telefone}
    contatos.append(contato)
    return contato
