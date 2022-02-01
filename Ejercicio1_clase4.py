number = 0.0
number = float(input('Ingrese una cantidad: '))

par = number % 2 == 0
positivo = number > 0 

message = f'El número: {number} ' 

if par:
    message += 'es par y '
else:
    message += 'es impar y ' 

if positivo:
    message += 'positivo'
else:
    message += 'negativo'

print(message)