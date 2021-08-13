# https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main/32185 #

## Prueba ejecutar el archivo holaMundo.py y luego el archivo modulo.py ##
import modulo

def main():
    print('Hola Mundo desde principal!')

if __name__ == '__main__':
    main()
    modulo.holaMundo()