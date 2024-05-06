import time
import os

def interface_movimientos_fn():
    print("Bienvenido al Banco de Ingenieros")
    print("Movimientos disponibles:")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir\n")

    try:
        option = int(input("Ingrese una opcion: "))
        if option < 0 or option > 4:
            raise ValueError
        
        time.sleep(1.2)
        os.system('cls')
        return option
    except ValueError:
        print("Opcion invalida")
        time.sleep(2.5)
        os.system('cls')
        return interface_movimientos_fn()