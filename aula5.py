texto = """1
8
9
0
1"""
lista = texto.split('\n')
soma = 0 
for numero in lista: 
	soma += int(numero)
media = soma/len(lista)
print(media)