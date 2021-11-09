class Tienda():
    def __init__(self, remera, pantalon, vestido):
        self._remera = remera
        self._pantalon = pantalon
        self._vestido = vestido
        
    def prendas(self):
        print("Las prendas que tengo disponibles son: \n")
        self._remera.remera()
        self._pantalon.pantalon()
        self._vestido.vestido()        
