# productos = {codigo: [tipo, nombre, sabor, tamano, vegano], ...}

productos = {
    'TRT01': ['Torta',   'Selva Negra',    'Chocolate',   'Grande',     'No'],
    'TRT02': ['Torta',   'Tres Leches',    'Vainilla',    'Mediana',    'No'],
    'GAL01': ['Galleta', 'Chips de Choco', 'Chocolate',   'Individual', 'No'],
    'GAL02': ['Galleta', 'Avena y Pasas',  'Avena',       'Individual', 'Si'],
    'PAN01': ['Pan',     'Baguette',       'Natural',     'Grande',     'Si'],
    'PAN02': ['Pan',     'Croissant',      'Mantequilla', 'Individual', 'No'],
    'BEB01': ['Bebida',  'Cafe Latte',     'Cafe',        'Mediano',    'No'],
    'BEB02': ['Bebida',  'Jugo Natural',   'Naranja',     'Grande',     'Si'],
}

# inventario = {codigo: [precio, cantidad], ...}

inventario = {
    'TRT01': [18990, 3],
    'TRT02': [15990, 2],
    'GAL01': [1290, 40],
    'GAL02': [1390, 25],
    'PAN01': [1990, 15],
    'PAN02': [1490, 30],
    'BEB01': [3490, 12],
    'BEB02': [2990, 8],
    'TRT09': [21990, 0],
}


def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Stock por tipo")
    print("2. Busqueda por precio")
    print("3. Agregar producto")
    print("4. Actualizar precio")
    print("5. Eliminar producto")
    print("6. Salir")


def elegir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opcion valida")
        except ValueError:
            print("Debe ingresar un numero entero")


def stock_tipo(tipo, productos, inventario):
    stock = 0
    for clave, valor in productos.items():
        if valor[0].strip().lower() == tipo.strip().lower():
            stock += inventario[clave][1]
    
    print(f"El stock del tipo {tipo} es: {stock}")


def busqueda_precio(p_min, p_max, productos, inventario):
    lista = []
    for clave, valor in inventario.items():
        if valor[0] >= p_min and valor[0] <= p_max and valor[1] != 0:
            tipo = productos[clave][0]
            lista.append(f"{tipo}--{clave}")
    lista.sort()
    return lista

def buscar_por_codigo(codigo, productos):
    if codigo in productos:
        return True
    else:
        return False
    

def agregar_producto(codigo, tipo, nombre, sabor, tamano, es_vegano, precio, cantidad, productos, inventario):
    if buscar_por_codigo(codigo, productos):
        return False
    else:
        valor_producto = [tipo, nombre, sabor, tamano, es_vegano]
        valor_inventario = [precio, cantidad]
        productos[codigo] = valor_producto
        inventario[codigo] = valor_inventario
        return True

def actualizar_precio(codigo, precio, productos, inventario):
    if buscar_por_codigo(codigo, productos) == False:
        return False
    else:
        inventario[codigo][0] = precio
        return True


def eliminar_producto(codigo, productos, inventario):
    if buscar_por_codigo(codigo, productos) == False:
        return False
    else:
        del productos[codigo]
        del inventario[codigo]
        return True


def main():
    while True:
        menu()
        opcion = elegir_opcion()

        if opcion == 1:
            tipo = input("Ingrese el tipo a consultar: ")
            stock_tipo(tipo, productos, inventario)
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingredsar valores enteros!!")

            lista = busqueda_precio(p_min, p_max, productos, inventario)
            if len(lista) > 0:
                print(lista)
            else:
                print("No hay productos en ese rango de precios.")
        elif opcion == 3:
            codigo_producto = input("Ingrese el codigo: ")
            tipo_producto = input("Ingrese el tipo: ")
            nombre_producto = input("Ingrese el nombre del producto: ")
            sabor_producto = input("Ingrese el sabor del producto: ")
            tamano_producto = input("Ingrese el tamaño del producto: ")
            es_vegano = input("Ingrese si el producto es vegano (Si/No): ")

            while True:
                try:
                    precio = int(input("Ingrese el precio del producto: "))
                    break
                except ValueError:
                    print("Debe ingresar un numero entero")
            
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    break
                except ValueError:
                    print("Debe ingresar un numero entero")


            if agregar_producto(codigo_producto, tipo_producto, nombre_producto, sabor_producto, tamano_producto, es_vegano, precio, cantidad, productos, inventario):
                print("Producto agregado!!")
            else:
                print("Producto ya existe!!")

        elif opcion == 4:
            codigo = input("Ingrese el codigo del producto que desea actualiar: ")
            while True:
                try:
                    precio_nuevo = int(input("Ingrese el nuevo precio: "))
                    break
                except ValueError:
                    print("Debe ingresar un numero entero")

            if actualizar_precio(codigo, precio_nuevo, productos, inventario) == True:
                print("Precio actualizado!!")
            else:
                print("El producto no existe")
        elif opcion == 5:
            codigo_eliminar = input("Ingrese el codigo del producto que desea eliminar: ")
            if eliminar_producto(codigo_eliminar, productos, inventario) == True:
                print("Producto eliminado!!")
            else:
                print("El producto no existe!!")
        elif opcion == 6:
            print("Programa finalizado.")
            break
        



main()