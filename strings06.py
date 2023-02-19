#conte quantos espaços em branco existem na frase, e quantas vezes as vogais aparecerem na frase
frase = str(input('digite algo:'))
branco = frase.count(" ")
print('Na frase "{}", contém {} espaços em branco'.format(frase, branco))
print('na sua frase contem {} letras A\n{} letras E\n{} letras I\n{} letras O\ne {} LETRAS U'.format(frase.count('a'), frase.count('e'), frase.count('i'), frase.count('o'), frase.count('u')))

