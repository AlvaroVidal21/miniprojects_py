import pickle
import time
import os


def crear_binario(data, ruta: str):
    with open(ruta, 'wb') as file:
        pickle.dump(data, file)


def cargar_binario(ruta: str):
    with open(ruta, 'rb') as file:
        data = pickle.load(file)
        return data


def enlistar_data(Clase: object):
    data_list = [
        Clase.nombre,
        Clase._tipo_cuenta,
        Clase.saldo
    ]

    return data_list


def clasificar_data(data_list: list, nombre_clase: str, Clase: object):
    # Crea la clase
    nombre_clase = Clase(data_list[0])
    # Asigna el saldo
    nombre_clase.depositar = data_list[2]

    return nombre_clase
