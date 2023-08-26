import random
from pyfiglet import Figlet

figlet = Figlet()
fuentes_disponibles = figlet.getFonts()

print("Fuentes disponibles:")
for fuente in fuentes_disponibles:
    print(fuente)

fuente_elegida = input("Ingrese el nombre de la fuente que desee usar, si quiere elegir una de forma aleatoria deje el espacio en blanco: ")

if not fuente_elegida:
    fuente_seleccionada = random.choice(fuentes_disponibles)
elif fuente_elegida not in fuentes_disponibles:
    print("La fuente elegida no está disponible")
else:
    fuente_seleccionada = fuente_elegida

figlet.setFont(font=fuente_seleccionada)
texto = input("Ingrese el texto a imprimir: ")

print(figlet.renderText(texto))
