from abc import ABC, abstractmethod


class CuentasBancarias(ABC):
    def __init__(self, nombre, apellido, saldo, comision = False):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo
        self.comision = comision


    @abstractmethod
    def ver_saldo(self):
        print(f'Saldo: S/{self.saldo}')
        return self.saldo



class CuentaAhorros(CuentasBancarias):
    def __init__(self, nombre, apellido, saldo, comision = False, interes = 0.045):
        super().__init__(nombre, apellido, saldo, comision = False)

        self.interes = interes
        # self.comision = comision


    def agregar_interes(self):
        self.saldo = self.saldo + (self.saldo * self.interes)
        return self.saldo


    def ver_saldo(self):
        print(f'Saldo: S/{self.saldo}')
        return self.saldo



