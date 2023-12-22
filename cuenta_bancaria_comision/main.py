from cuentas_bancarias import CuentasBancarias, CuentaAhorros
from asignador_de_saldo import asignador_de_saldo as saldo_aleatorio
from clientes import clientes_bancarios

CLIENTES = clientes_bancarios

# Iteramos sobre los clientes bancarios y vamos generando cuentas bancarias 

clientes_asignados = []

id_client = 0 # id para asignar a cada cliente
for cliente in CLIENTES:
    cliente_nuevo = 'cliente' + str(id_client)
    cliente_nuevo = CuentaAhorros(cliente['nombre'], cliente['apellido'], saldo_aleatorio())
    clientes_asignados.append(cliente_nuevo)
    id_client += 1 # al instanciar cada cliente sería: cliente0, cliente1, cliente2, etc.
    
print('Clientes asignados')





def run():
    print('Bienvenido a Banco Python')
    print('-----' * 10)
    print("clientes_asignados: ")
    for c in clientes_asignados:
        print(f'Nombre: {c.nombre} {c.apellido}\n Saldo: S/{c.saldo}')
        print('-----' * 10)


if __name__ == '__main__':
    run()