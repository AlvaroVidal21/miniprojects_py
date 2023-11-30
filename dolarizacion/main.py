# MODULES

import clients 
from packages.dollarizer import dollarizer



# INSTANCIAR CLIENTES

client_001 = clients.BankingClients('Sherlock Holmes', 10000)
client_002 = clients.BankingClients('John Watson', 20000, 1)
client_003 = clients.BankingClients('Mycroft Holmes', 30000, 2)
client_004 = clients.BankingClients('Mary Watson', 40000, 3)


list_of_clients = [client_001, client_002, client_003, client_004]






def run():
    clients_dollarized =  dollarizer(list_of_clients)

    for client in clients_dollarized:
        print(client.name)
        print(client.amount)
        print(client.bank)
        print('---------------------')



   


if __name__ == '__main__':
    run()