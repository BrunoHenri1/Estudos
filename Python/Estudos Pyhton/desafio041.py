from datetime import date
atual = date.today().year

ano = int(input("Digite o Ano de nascimento do atleta: "))
idade = atual - ano
print("O atleta tem {} anos.".format(idade))

if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <=25:
    print("CLassificação: SÊNIOR")
elif idade >= 26:
    print("Classificação MASTER!")
