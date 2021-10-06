class Padre():
    def saludar(self):
        print('Hola')

class Madre():
    def saludar(self):
        print('Weena')

class Hijo(Padre, Madre):
    def saludar(self):
        Padre().saludar()
        Madre().saludar()
        print('Chao')

yo = Hijo()
yo.saludar()