class Vestido():
    def __init__(self, material, marca, tipo):
        self._material = material
        self._marca = marca
        self._tipo = tipo

    def vestido(self):
        pass
class VestidoZara(Vestido):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def vestido(self):
        print(f"VESTIDO MARCA:  {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")

class VestidoKosiuko(Vestido):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def vestido(self):
        print(f"VESTIDO MARCA:  {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")

class VestidoJazmin(Vestido):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def vestido(self):
        print(f"VESTIDO MARCA:  {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")