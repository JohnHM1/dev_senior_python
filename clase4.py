ventasTotales = 0


numProductos = int(input("Ingrese el numero de productos: "))


nombres=[]
precios=[]
cantidades=[]


print("Ingreso inicial de productos: ")
for i in range(numProductos):
    print(f"Producto {i+1}: ")
    productName = input("Ingrese el numero del producto: ").lower()
    nombres.append(productName)
    productCost = float(input("Digite el precio del producto: "))
    precios.append(productCost)
    unids = int(input("Digite el numero de unidades: "))
    cantidades.append(unids)


while True:
    print("\n --MENU DROGUERIA--")
    print("\n 1.Vernder Producto")
    print("\n 2.Mostrar Inventario")
    print("\n 3.Mostrar Ventas Totales")
    print("\n 4.Salir")


    select = int(input("Ingrese una opcion: "))
    if select == 1:


        print("\n Vernder Producto:")    
        sellName = input("Ingrese el nombre del producto: ").lower()
        sellUnids = int(input("Ingrese la cantidad: "))


        findProduct = False
        for i in range(len(nombres)):
            if nombres[i] == sellName:
                findProduct=True
                if sellUnids <= cantidades[i]:
                    totalySell = sellUnids*precios[i]
                    ventasTotales+=totalySell
                    cantidades[i]-=sellUnids
                    print(f"Venta Realizada. Total Venta: {totalySell:.2f}")# Con :.2f reducimos el total de numeros decimales a 2
                    print(f"Quedan {cantidades[i]} de {nombres[i]} en el inventario.")
                else:
                    print(f"Cantidad insuficiente. Hay {cantidades[i]}.")
                break
        if not findProduct:
            print("Producto no encontrado.")


    elif select == 2:

        print("\n Inventario de productos: ")
        

        for i in range(len(nombres)):
            print(f"Procducto {i+1}: {nombres[i].capitalize()}, el precio $ {precios[i]:.2f}, Cantidad: {cantidades[i]}")


    elif select == 3:
        print(f"Ventas totales a cumuladas : ${ventasTotales}")
        
    elif select == 4:
        break