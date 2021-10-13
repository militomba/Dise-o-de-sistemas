from banco import *
from ejecutivoCuenta import *
from LiderTeamEjecutivo import *
from gerente import *
from director import *

if __name__=="__main__":

    banco = Banco()

    monto = 150000

    banco.ejecutivoCuenta.solicitudPrestamo(monto)

