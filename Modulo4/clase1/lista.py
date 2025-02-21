#app de gestion de pediodos de una tienda

def agregarPedido(pedidos: list[str], nuevoPedido: str)-> list[str]:
    pedidos.append(nuevoPedido)
    return pedidos

def eliminarPedido(pedidos: list[str], pedidoAEliminar: str)-> list[str]:
    if pedidoAEliminar in pedidos:
        pedidos.remove(pedidoAEliminar)
        return pedidos
    else:
        print("Pedido no encontrado")
        return pedidos

def buscarPedido(pedidos: list[str], pedidoABuscar: str)-> int:
    if pedidoABuscar in pedidos:
        return pedidos.index(pedidoABuscar)+1
    else:
        print("Pedido no encontrado")
        return -1
    
def main():
    # Inicializamos la lista de pedidos
    pedidosTienda = ["Pedido 1", "Pedido 3"]

    # Agregamos un nuevo pedido 
    pedidosTienda = agregarPedido(pedidosTienda, "Pedido 2")
    print(f'Lista de pedidos actual: {pedidosTienda}')

    # Eliminamos un pedido
    pedidosTienda = eliminarPedido(pedidosTienda, "Pedido 1")
    print(f'Lista de pedidos actual: {pedidosTienda}')

    #Ordenamos la lista de pedidos
    pedidosTienda.sort()
    print(f'Lista de pedidos actual: {pedidosTienda}')

    # Buscamos un pedido
    pedidoABuscar= "Pedido 3"
    posicionPedido = buscarPedido(pedidosTienda, pedidoABuscar)
    if posicionPedido!= -1:
        print(f"Pedido {pedidoABuscar} se encuentra en la posición {posicionPedido}")


if __name__ == "__main__":
    main()