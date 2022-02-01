player1 = input('Jugador 1: escoja su jugada: 1 (Piedra), 2 (papel) o 3 (tijeras): ')
player2 = input('Jugador 2: escoja su jugada: 1 (Piedra), 2 (papel) o 3 (tijeras): ')

if player1 == '1' and player2 == '3':
    message = 'El jugador 1 gana'
elif player1 == '3' and player2 == '2':
    message = 'El jugador 1 gana'
elif player1 == '2' and player2 == '1':
    message = 'El jugador 1 gana'

if player2 == '1' and player1 == '3':
    message = 'El jugador 2 gana'
elif player2 == '3' and player1 == '2':
    message = 'El jugador 2 gana'
elif player2 == '2' and player1 == '1':
    message = 'El jugador 2 gana'

if player2 == '1' and player1 == '1':
    message = 'Empate'
elif player2 == '3' and player1 == '3':
    message = 'Empate'
elif player2 == '2' and player1 == '2':
    message = 'Empate'

print(message)