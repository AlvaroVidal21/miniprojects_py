from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, nombre:str):
        self.nombre = nombre
        self._tipo_cuenta = 'Cuenta Bancaria'
        self.__saldo = 0


    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def depositar(self, monto:float):
        self.__saldo += monto

    @saldo.setter
    def retirar(self, monto:float):
        self.__saldo -= monto

    @abstractmethod
    def generar_interes(self, interes:float):
        pass



class CuentaAhorros(CuentaBancaria):
    def __init__(self, nombre:str):
        super().__init__(nombre)
        self.interes = 0.065
        self._tipo_cuenta = 'Cuenta Ahorros'
    def generar_interes(self):
        saldo_actual = self.saldo
        interes_generado = saldo_actual * self.interes
        self.depositar = interes_generado



