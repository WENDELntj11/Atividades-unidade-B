itens_menu = {"Pizza": 25.99, "Sushi": 40.99, "refrigerantes": 7.50, "Barca de acai": 20.99, "Porcoes de fritos": 35.99}
pedidos = {}

def adicionar_pedido(numero_pedido, itens):
    pedidos[numero_pedido] = itens

def adicionar_item_pedido(numero_pedido, item, quantidade):
    if numero_pedido in pedidos:
        if item in itens_menu:
            pedidos[numero_pedido][item] = quantidade
        else:
            print(" Infelizmente este item não está no menu.")
    else:
        print('Pedido não  foi encontrado.')

def calcular_total(numero_pedido):
    total = 0
    for item, quantidade in pedidos[numero_pedido].items():
        total += itens_menu[item] * quantidade
    return total

adicionar_pedido(1, {"Pizza": 3})
adicionar_item_pedido(1, {"Sushi"}, 2)
adicionar_item_pedido(1, {"refrigerantes"}, 2)
adicionar_item_pedido(1, {"Barca de acai"}, 2)
adicionar_item_pedido(1, {"Porcoes de fitos"}, 2)
print(calcular_total(1))