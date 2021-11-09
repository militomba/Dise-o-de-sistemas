from tienda import *
from remera import*
from pantalon import*
from vestido import *

def main():
    remera1 = RemeraJazmin("Algodon", "Jazmin Chebar", "Remera manga corta con cuello redondo")
    pantalon1 = PantalonZara("Jean", "Zara", "Pantalon chupin roto en las rodillas")
    vestido1 = VestidoKosiuko("Algodon", "Kosiuko", "Vestido apretado corto")
    tienda = Tienda(remera1, pantalon1, vestido1)
    tienda.prendas()

if __name__=="__main__":
    main()