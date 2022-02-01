name = input('Ingrese su nombre: ')
edad = int(input('ingrese su edad: '))

message = f'El cliente: {name} tiene:  {edad} años y su entrada de cine'

if 0 < edad <= 4:
    message +='es gratis'
elif 4 < edad <= 18:
    message += 'cuesta: $1.50'
elif 18 < edad <= 60:
    message += 'cuesta: $2.00'
elif edad > 60:
    message += 'cuesta: $1.00'

print(message)