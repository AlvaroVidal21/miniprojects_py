from CuentaBancaria_Clase.cuentabancaria import *
# Interfaces
from interfaces.interface_movimientos import *
# Binarios actions
from actions.pickle_actions import *
# Movimientos financieros
from actions.movimientos import *

import os

PATH_URL = 'data/data'


def doing():

    if not os.path.isfile(PATH_URL):
        # Instanciar
        c001 = CuentaAhorros('Alva Vidal')
        # Crear el binario inicial
        data = enlistar_data(c001)
        crear_binario(data, PATH_URL)

    else:
        # Interfaz
        option = interface_movimientos_fn()
        if option == 1:
            ver_saldo(CuentaAhorros, cargar_binario, crear_binario, enlistar_data, PATH_URL, clasificar_data)
        elif option == 2:
            depositar(CuentaAhorros, cargar_binario, crear_binario, enlistar_data, PATH_URL, clasificar_data)
        elif option == 3:
            retirar(CuentaAhorros, cargar_binario, crear_binario, enlistar_data, PATH_URL, clasificar_data)
        else:
            exit()


if __name__ == '__main__':
    doing()