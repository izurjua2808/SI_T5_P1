import keyboard es para añadir la libreria de keyboard que hemos instalado con el comando "pip install keyboard"

Luego definimos una función a la que llamaremos TeclasPresionadas, y añadimos una variable llamada tecla.

Cuando se pulsa una tecla, se escribirá la tecla en otro archivo, por ejemplo si presionamos la tecla x saldría "x", si presionamos la tecla espacio saldra "space".

print(tecla.name)

Para guardar todas las teclas presionadas lo haremos con with open("texto.txt", "a") as file
"a" es para que se añada lo que escribimos al final del texto y no se sobreescriba.


if tecla.name == 'space': 
file.write(' ')
Esta linea permite que cuando pulsemos la tecla espacio, en vez de que escriba "space", ponga un espacio de verdad.

else:
file.write(tecla.name)
Esta linea dice que si no se pulsa el espacio, no haga lo de arriba y solo ponga el nombre de la tecla

keyboard.on_press(TeclasPresionadas) Hace que quede registrada la tecla que se pulsa

keyboard.wait() Nos deja el programa abierto y espera a que se pulse alguna tecla