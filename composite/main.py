from abc import ABCMeta, abstractmethod, abstractstaticmethod


class IEmpresa(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employee, sueldo):
        """Implement en clase hija"""


    @abstractstaticmethod
    def print_employee(self):
        """implement en clase hija"""
    
    @abstractstaticmethod
    def print_sueldo(self):
        """implement en clase hija"""

class Gerente(IEmpresa):

    def __init__(self, employee, sueldo):
        self.employee = employee
        self.sueldo = sueldo

    def print_employee(self):
        print(f"GERENTES DE LA EMPRESA: {self.employee}")
    
    def print_sueldo(self):
        print(f"SUELDO DEL GERENTE: ${self.sueldo}")
        

class Desarrolladores(IEmpresa):

    def __init__(self, employee, sueldo):
        self.employee = employee
        self.sueldo = sueldo

    def print_employee(self):
        print(f"DESARROLLADORES DE LA EMPRESA: {self.employee}")

    def print_sueldo(self):
        print(f"SUELDO DEL DESARROLLADOR: ${self.sueldo}")

class Tecnicos(IEmpresa):
    def __init__(self, employee, sueldo):
        self.employee = employee
        self.sueldo = sueldo
    
    def print_employee(self):
        print(f"TECNICOS DE LA EMPRESA: {self.employee}")

    def print_sueldo(self):
        print(f"SUELDO DEL TECNICO: ${self.sueldo}")        

class ParentEmpresa(IEmpresa):
    def __init__(self, employee, sueldo):
        self.employee = employee
        self.sub_empresas = []
        self.sueldo = sueldo
    

    def add(self, empresa):
        self.sub_empresas.append(empresa)
        self.employee += empresa.employee
        self.sueldo += empresa.sueldo

    def print_employee(self):
        for empresas in self.sub_empresas:
            empresas.print_employee()
            #empresas.print_sueldo()
        print(f"NÚMERO TOTAL DE EMPLEADOS: {self.employee}")
        #print(f"Número de sueldos totales: {self.sueldo}")
    def print_sueldo(self):
        for empresas in self.sub_empresas:
            empresas.print_sueldo()
        print(f"SUMA DE SUELDOS: ${self.sueldo} ")

        

empleados1 = Gerente(30,80000)
empleados2 = Desarrolladores(150,75000)
empleado3 = Tecnicos(140,67000)

parent_empleados = ParentEmpresa(0,0)

parent_empleados.add(empleados1)
parent_empleados.add(empleados2)
parent_empleados.add(empleado3)

parent_empleados.print_employee()
parent_empleados.print_sueldo()