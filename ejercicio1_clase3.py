rain = 5e6
rain = rain * (1-0.1)
volumen_reservorio = 4.445e8
volumen_reservorio = volumen_reservorio * (1-5/100) 
volumen_reservorio = volumen_reservorio * (1-0.02) 
volumen_reservorio -= 2.5e5
print(volumen_reservorio)