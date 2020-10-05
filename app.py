print('¿que quieres hacer?')
print()
print('escribe suma si quieres sumar escribe resta si quieres restar escribe multiplicar si quieres multiplicar o escribe dividir para dividir')

operador = input()
sun = 'suma'
res = 'resta'
multi = 'multiplicar'
div = 'dividir'


if sun == str(operador):
	num1 = int(input('Dame el primmer numero '))
	num2 = int(input('Dame el segundo numero '))
	add = num1+num2
	print(add)

elif div == str(operador):
	d1 = int(input('Dame el primmer numero '))
	d2 = int(input('Dame el primmer numero '))
	dev = d1/d2
	print(dev)

elif multi == str(operador):
	n1 = int(input('Dame el primer numero '))
	n2 = int(input('Dame el segundo numero '))
	mul = n1*n2
	print(mul)

elif res == str(operador):
	nu1 = int(input('Dame el primer numero '))
	nu2 = int(input('Dame el segundo numero '))
	menos = nu1-nu2
	print(menos)

else:
	print('no haz espesificado tu operacion')