class Libro:
    def __init__(self, estado, titulo):
       self.estado=estado 
       self.titulo=titulo
        
    #get y set
    
    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado):
        self._estado=estado
    
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo=titulo