# 097: Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensag
# com tamanho adaptável.
def escreva(msg):
    tam = len(msg) + 4
    print('-'* tam)
    print(f'  {msg}')
    print('-'* tam)
    

escreva('Rebeca Nascimento')
escreva('Rener Silva')
