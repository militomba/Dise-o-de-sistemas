from abc import abstractstaticmethod


class IAprobador():
            
    @abstractstaticmethod
    def set_next(self):
        pass

    @abstractstaticmethod
    def solicitudPrestamo(self, monto):
        pass