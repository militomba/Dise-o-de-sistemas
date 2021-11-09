class Pantalon():
    def __init__(self, material, marca, tipo):
        self._material = material
        self._marca = marca
        self._tipo = tipo

    def pantalon(self):
        pass
class PantalonZara(Pantalon):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def pantalon(self):
        print(f"PANTALON MARCA:  {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")

class PantalonKosiuko(Pantalon):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def pantalon(self):
        print(f"PANTALON MARCA:  {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")

class PantalonJazmin(Pantalon):
    def __init__(self, material, marca, tipo):
        super().__init__(material, marca, tipo)
    def pantalon(self):
        print(f"PANTALON MARCA:  {self._marca}, MATERIAL: {self._material}, DESCRIPCION: {self._tipo}")