from cliente import *

def main():
    cli = Cliente()
    print("Nike: ")
    cli.cliente(NikeFabica())
    print("\n Adidas: ")
    cli.cliente(AdidasFabica())

if __name__=="__main__":
    main()