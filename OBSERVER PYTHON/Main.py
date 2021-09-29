from Biblioteca import Biblioteca
from Libro import Libro

if __name__ == "__main__":
    Biblioteca.devuelve_libro(Libro("Libro1", "MALO"))
    Biblioteca.devuelve_libro(Libro("Libro2", "BUENO"))