puntos = int(input('Ingrese su puntuación: '))



if puntos >= 1 and puntos <= 50:
    message = f"No hay premios para {puntos} pts"
elif puntos >= 51 and puntos <= 150:
    message = f"Felicitaciones, Ganaste la medalla de Bronce por haber tenido {puntos} pts!"
elif puntos >= 151 and puntos <= 180:
    message = f"Felicitaciones, Ganaste la medalla de Plata por haber tenido {puntos} pts!"
elif puntos >= 181 and puntos <= 200:
    message = f"Felicitaciones, Ganaste la medalla de Oro por haber tenido {puntos} pts!"
medal = 'Oro'

print(message)


 
 
 
 
