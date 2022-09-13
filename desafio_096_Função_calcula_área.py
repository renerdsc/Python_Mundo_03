#096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.
def área(larg, compri):
    soma = larg * compri
    print(f'A área de um terrno {larg} x {compri} é de {soma} m².')


la = float(input('digite a largura do terreno:'))
co = float(input('Digite o comprimento do terreno:')) 
área(la, co)
