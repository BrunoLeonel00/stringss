# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
f1 = str(input('Digite algo:')).strip()
f2 = str(input('DIgite algo:')).strip()

print('O tamanho de "{}" tem: {} caracteres'.format(f1, len(f1)))
print('o tamanho de "{}" tem: {} caracteres'.format(f2, len(f2)))
if len(f1) == len(f2):
    print('as duas strings tem tamanhos iguais')
    print('as duas strings tem conteudos iguais')
else:
    print('as duas strings tem tamanhos diferentes')
    print('as duas strings tem conteudos difentes ')

