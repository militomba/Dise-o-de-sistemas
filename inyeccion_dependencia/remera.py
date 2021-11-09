class Remera():
    def __init__(self, material, marca, tipo):
        self._material = material
        self._marca = marca
        self._tipo = tipo

    def remera(self):
        pass
class RemeraZara(Remera):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def remera(self):
        print(f"REMERA MARCA: {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")

class RemeraKosiuko(Remera):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def remera(self):
        print(f"REMERA MARCA: {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")

class RemeraJazmin(Remera):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def remera(self):
        print(f"REMERA MARCA: {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")

