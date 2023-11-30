DOLLAR = 3.74


def dollarizer(list_of_clients):
    """Converts a client's balance from soles to dollars."""
    for client in list_of_clients:
        client.amount = client.amount * DOLLAR

    return list_of_clients
