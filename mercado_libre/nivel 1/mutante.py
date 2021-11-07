import numpy as np
from numpy.lib.twodim_base import diag

contador = 0


#matriz
adn = np.array([["A","T","G","C","G","A"],
                ["C","A","G","T","G","C"],
                ["T","T","A","T","G","T"],
                ["A","G","A","A","G","G"],
                ["C","C","C","C","T","A"],
                ["T","C","A","C","T","G"]])
#print(adn)

#secuencia
A=['A','A','A','A']
T=['T','T','T','T']
G=['G','G','G','G']
C=['C','C','C','C']

def diagonales():
    global contador

    #DIAGONALES        
    diagonal_ppal = np.diag(adn)
    diagonal_superior1 = np.diag(adn, k=1)
    diagonal_superior2 = np.diag(adn, k =2)
    diagonal_inferior1 = np.diag(adn,k=-1)
    diagonal_inferior2 = np.diag(adn, k=-2)



#diagonal principal
   
    # posicion 0 a 4
    if list(diagonal_ppal[0:4]) == A or list(diagonal_ppal[0:4]) == T or list(diagonal_ppal[0:4]) == C or list(diagonal_ppal[0:4]) == G:
        contador +=1

    #posicion 1 a 5
    elif list(diagonal_ppal[1:5]) == A or list(diagonal_ppal[1:5]) == T or list(diagonal_ppal[1:5]) == C or list(diagonal_ppal[1:5]) == G:
        contador +=1

    #posicion 2 a 6
    elif list(diagonal_ppal[2:6]) == A or list(diagonal_ppal[2:6]) == T or list(diagonal_ppal[2:6]) == C or list(diagonal_ppal[2:6]) == G:
        contador +=1

#diagonal superior 1
    elif list(diagonal_superior1[0:4]) == A or list(diagonal_superior1[0:4]) == T or list(diagonal_superior1[0:4]) == C or list(diagonal_superior1[0:4]) == G:
        contador +=1

    #posicion 1 a 5
    elif list(diagonal_superior1[1:5]) == A or list(diagonal_superior1[1:5]) == T or list(diagonal_superior1[1:5]) == C or list(diagonal_superior1[1:5]) == G:
        contador +=1    


#diagonal inferior 1
    elif list(diagonal_inferior1[0:4]) == A or list(diagonal_inferior1[0:4]) == T or list(diagonal_inferior1[0:4]) == C or list(diagonal_inferior1[0:4]) == G:
        contador +=1

    #posicion 1 a 5
    elif list(diagonal_inferior1[1:5]) == A or list(diagonal_inferior1[1:5]) == T or list(diagonal_inferior1[1:5]) == C or list(diagonal_inferior1[1:5]) == G:
        contador +=1 

#diagonal superior2
    elif list(diagonal_superior2) == A or list(diagonal_superior2) == T or list(diagonal_superior2) == C or list(diagonal_superior2) == G:
        contador +=1

#diagonal inferior 2
    elif list(diagonal_inferior2) == A or list(diagonal_inferior2) == T or list(diagonal_inferior2) == C or list(diagonal_inferior2) == G:
        contador +=1


def filas():
    global contador
    for i in adn:
        f1=list(i[0:4])
        f2=list(i[1:5])
        f3=list(i[2:6]) 
        if f1 == A or f1 == T or f1 == C or f1 == G:
            contador +=1
        if f2 == A or f2 == T or f2 == C or f2 == G:
            contador +=1
        if f3 == A or f3 == T or f3 == C or f3 == G:
            contador +=1
        


def columnas():
    global contador
    matriz = np.transpose(adn)
    for i in matriz:
        c1=list(i[0:4])
        c2=list(i[1:5])
        c3=list(i[2:6]) 
        if c1 == A or c1 == T or c1 == C or c1 == G:
            contador +=1
        if c2 == A or c2 == T or c2 == C or c2 == G:
            contador +=1
        if c3 == A or c3 == T or c3 == C or c3 == G:
            contador +=1

def is_mutant():
    global contador
    if contador >= 2:
        print("--Es mutante--")
    else:
        print("--Es humano--")

if __name__ == "__main__":
    diagonales()
    filas()
    columnas()
    is_mutant()








    


    



