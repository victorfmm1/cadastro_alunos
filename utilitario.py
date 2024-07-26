from aluno import Cadastro
from nota import Notas
from media import Media

LISTA_ALUNO = []
LISTA_PAIS = []
LISTA_IDADES = []
LISTA_NOTA1 = []
LISTA_NOTA2 = []
LISTA_MEDIA = []

def cadastar_aluno(nome, nome_pai, idade):
    novo_aluno = Cadastro(
        nome = nome,
        nome_pai = nome_pai,
        idade = idade )

    LISTA_ALUNO.append(novo_aluno)
    return novo_aluno


def lancar_nota1(nota1):
    nova_nota1 = Notas(nota1 = nota1)
    if nota1 < 0 or nota1 > 10:
        raise ValueError("Nota 1 deve estar entre 0 e 10.")

    LISTA_NOTA1.append(nova_nota1)
    return nova_nota1


def lancar_nota2(nota2):
    nova_nota2 = Notas(nota2 = nota2)
    if nota2 < 0 or nota2 > 10:
        raise ValueError("Nota 2 deve estar entre 0 e 10.")

    LISTA_NOTA2.append(nova_nota2)
    return nova_nota2

def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    if media < 6:
        print(f"Media: {media} está reprovado")
    else:
        print(f"Media: {media} está aprovado")

    LISTA_MEDIA.append(media)
    return media

def exibir_nota1():
    print(LISTA_NOTA1)

def exibir_nota2():
    print(LISTA_NOTA2)

def exibir_media():
    print(LISTA_MEDIA)