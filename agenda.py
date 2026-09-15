import json

ARQUIVO = "contatos.json"


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


def remover_contato(contatos, nome):
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contatos.remove(contato)
            return True
    return False


def salvar_contatos(contatos, caminho=ARQUIVO):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, ensure_ascii=False, indent=2)


def carregar_contatos(caminho=ARQUIVO):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
