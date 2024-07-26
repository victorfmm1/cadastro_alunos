from utilitario import (
    cadastar_aluno,
    lancar_nota1,
    lancar_nota2,
    calcular_media,
    exibir_media,
    exibir_nota1,
    exibir_nota2
)

#cadastrar aluno
cadastar_aluno(
    nome = input("Nome:"),
    nome_pai = input("Nome pai:"), 
    idade = int(input("Idade:"))
    ) 

# lançar nota1
nota1 = float(input("Nota 1:"))
lancar_nota1(nota1)

# lançar nota2
nota2 = float(input("Nota 2:"))
lancar_nota2(nota2)

# mostrar media
media = calcular_media(nota1, nota2)