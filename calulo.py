class Coodenada:
    def __init__ (self, x, y):
        self.x = x   
        self.y = y
    def distancia_puntos(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coodenada(3,30)
    coord_2 = Coodenada(4, 8)
    
    print(coord_1.distancia_puntos(coord_2))
