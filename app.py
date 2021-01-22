# -*- coding: utf-8 -*-
def main():
	print('¿Que quieres hacer?\n')#El '\n' es para dejar una linea en blanco aproposito.
	print('Escribe el nombre de la operacion que desees realizar en minusculas: ')

	operador = input()
	sun = 'suma'
	res = 'resta'
	multi = 'multiplicar'
	div = 'dividir'


	if sun == str(operador):
		num1 = int(input('Dame el primmer número: '))
		num2 = int(input('Dame el segundo número: '))
		add = num1+num2
		print(add)

	elif div == str(operador):
		d1 = int(input('Dame el primmer número: '))
		d2 = int(input('Dame el primmer número: '))
		dev = d1/d2
		print(dev)

	elif multi == str(operador):
		n1 = int(input('Dame el primer número: '))
		n2 = int(input('Dame el segundo número: '))
		mul = n1*n2
		print(mul)

	elif res == str(operador):
		nu1 = int(input('Dame el primer número: '))
		nu2 = int(input('Dame el segundo número: '))
		menos = nu1-nu2
		print(menos)

	else:
		print('No has especificado tu operación')

if __name__ == '__main__':
	main()
