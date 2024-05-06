# Serializacion en Python

Este proyecto busco poner en práctica los siguientes requerimientos:
- El **uso de serializacion** de listas en archivos binarios con la librería interna `pickle`.
- También utilizo el uso de decoradores para darle eficiencia al código.
- **Almacenamiento y lectura** de data mediante archivos binarios.
- **Uso de POO**: Clases, Herencias y Métodos abstractos mediante la librería `abc`.
- **Interfaces** mediante línea de comandos.

## Pequeños fragmentos 🧩

### Crear y leer binarios

```python
def crear_binario(data, ruta: str):
    with open(ruta, 'wb') as file:
        pickle.dump(data, file)


def cargar_binario(ruta: str):
    with open(ruta, 'rb') as file:
        data = pickle.load(file)
        return data
```

### Uso de decoradores
```python
def movimientos(movimiento: callable):
    def movimiento_func(Clase: object, 
    cargar_binario: callable, 
    crear_binario: callable, 
    enlistar_data: callable, 
    PATH_URL: str, 
    clasificar_data: callable):

        # Importar información
        data = cargar_binario(PATH_URL)  # Me devuelve una lista

        """
        Instancia CuentaAhorros con el saldo actual.
        Func: clasificar_data pide:
            lista = data
            nombre de la clase = c001
            clase = Objecto (CuentaAhorros)
        """
        c001 = clasificar_data(data, 'c001', Clase)
        
        # Movimiento: Ver, Depositar, Retirar
        movimiento(c001)

        # Exportar información
        data_list = enlistar_data(c001)
        crear_binario(data_list, PATH_URL)

    return movimiento_func


@movimientos
def ver_saldo(Cuenta: object):
    saldo_actual = Cuenta.saldo
    print(f'Su saldo actual es: {saldo_actual}')


@movimientos
def depositar(Cuenta: object):
    monto = float(input("Ingrese monto a depositar: "))
    Cuenta.depositar = monto


@movimientos
def retirar(Cuenta: object):
    monto = float(input("Ingrese monto a retirar: "))
    if monto > Cuenta.saldo:
        print("No tiene suficiente saldo")
    else:
        Cuenta.retirar = monto
```

### Métodos abstractos
```python
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
    # Obliga a que las clases hijas implementen este método
    def generar_interes(self, interes:float):
        pass
```