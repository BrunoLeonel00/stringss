# dizer se a frase é um polindromo ou nao
frase = str(input('digite algo:')).strip()
inverso = frase[::-1]
if inverso == frase:
    print('sim, a frase {} é um polindromo'.format(frase))
else:
    print('nao, a frase nao é um polindromo.')
    print('Para um frase ser um polindromo a leitura dela tem que ser indentica independente da forma lida.')


