

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
        Instancia CuentaAhorros con el saldo actual
        clasificar_data me pide:
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
