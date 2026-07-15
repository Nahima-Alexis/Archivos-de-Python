# plantas = {codigo: [tipo, nombre, color, luz, riego], ...}

plantas = {
    'SUC01': ['Suculenta', 'Echeveria',   'Verde',  'Alta',  'Bajo'],
    'SUC02': ['Suculenta', 'Jade',        'Verde',  'Alta',  'Bajo'],
    'INT01': ['Interior',  'Pothos',      'Verde',  'Media', 'Medio'],
    'INT02': ['Interior',  'Monstera',    'Verde',  'Media', 'Medio'],
    'EXT01': ['Exterior',  'Lavanda',     'Morado', 'Alta',  'Bajo'],
    'EXT02': ['Exterior',  'Rosal',       'Rojo',   'Alta',  'Alto'],
    'CAC01': ['Cactus',    'Cactus Bola', 'Verde',  'Alta',  'Bajo'],
    'FLO01': ['Flor',      'Orquidea',    'Blanco', 'Media', 'Medio'],
}

# inventario = {codigo: [precio, cantidad], ...}

inventario = {
    'SUC01': [3990, 20],
    'SUC02': [4490, 15],
    'INT01': [6990, 10],
    'INT02': [12990, 4],
    'EXT01': [5490, 8],
    'EXT02': [7990, 6],
    'CAC01': [3490, 25],
    'FLO01': [14990, 3],
    'FLO09': [19990, 0],
}




def menu():
    print("""
    *** MENU PRINCIPAL ***
    1. Stock por tipo
    2. Busqueda por precio
    3. Agregar planta
    4. Actualizar precio
    5. Eliminar planta
    6. Salir
    """)


def elegir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion >= 1 and opcion <=6:
                return opcion
            else:
                print("Debe ingresar una opcion valida")
        except ValueError:
            print("Debe ingresar un valor entero")

def stock_tipo(tipo, plantas, inventario):
    stock = 0
    for clave, valor in plantas.items():
        if valor[0].strip().lower() == tipo.strip().lower():
            stock+= inventario[clave][1]

    print(f"El stock de {tipo} es: {stock}")



def busqueda_precio(p_min, p_max, plantas, inventario):
    lista = []
    for clave, valor in inventario.items():
        if valor[0] >= p_min and valor[0] <= p_max and valor[1] != 0:
            tipo = plantas[clave][0]
            lista.append(tipo + "--" + clave)
    
    lista.sort()
    return lista



def buscar_por_codigo(codigo, inventario):
    if codigo in inventario:
        return True
    else:
        return False



def agregar_planta(codigo, tipo, nombre, color, nec_luz, riego, precio, cantidad, plantas, inventario):
    if buscar_por_codigo(codigo, inventario) == True:
        return False
    else:
        plantas[codigo] = [tipo, nombre, color, nec_luz, riego]    
        inventario[codigo] = [precio, cantidad]

        return True


def actualizar_precio(codigo, precio, inventario):
    if buscar_por_codigo(codigo, inventario) == False:
        return False
    else:
        inventario[codigo][0] = precio
        return True


def eliminar_planta(codigo, plantas, inventario):
    if buscar_por_codigo(codigo, inventario) == False:
        return False
    else:
        del plantas[codigo]
        del inventario[codigo]
        return True



def ejectutar_software():
    while True:
        menu()
        opcion = elegir_opcion()

        if opcion == 1:
            tipo = input("Ingrese el tipo del planta de la cual desea saber el stock: ")
            stock_tipo(tipo, plantas, inventario)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            
            lista = busqueda_precio(p_min, p_max, plantas, inventario)
            if len(lista) == 0:
                print("No hay plantas en ese rango de precios")
            else:
                print(lista)
        elif opcion == 3:
            codigo_nuevo = input("Ingrese el codigo: ")
            tipo_nuevo = input("Ingrese el tipo: ")
            nombre_nuevo = input("Ingrese el nombre: ")
            color_nuevo = input("Ingrese el color: ")
            nec_luz_nuevo = input("Ingrese necesidad de luz: ")
            riego_nuevo = input("Ingrese riego: ")

            while True:
                try:
                    precio_nuevo = int(input("Ingrese el precio: "))
                    break
                except ValueError:
                    print("Debe ingresar un numero entero")

            while True:
                try:
                    cantidad_nuevo = int(input("Ingrese la cantidad: "))
                    break
                except ValueError:
                    print("Deb ingresar un numero entero")
            
            if agregar_planta(codigo_nuevo, tipo_nuevo, nombre_nuevo, color_nuevo, nec_luz_nuevo, riego_nuevo, precio_nuevo, cantidad_nuevo, plantas, inventario) == True:
                print("Planta agregada!!")
            else:
                print("La planta ya existe!!")
        elif opcion == 4:
            codigo_actualizar = input("Ingrese el codigo de la planta que desea actualizar: ")
            while True:
                try:
                    precio = int(input("Ingrese el precio nuevo: "))
                    break
                except ValueError:
                    print("Debe ingresar un numero entero")

            if actualizar_precio(codigo_actualizar, precio, inventario) == True:
                print("Precio actualizado")
            else:
                print("La planta no existe")
        elif opcion == 5:
            codigo_eliminar = input("Ingrese el codigo de la planta que desea eliminar: ")
            if eliminar_planta(codigo_eliminar, plantas, inventario) == True:
                print("Planta eliminada")
            else:
                print("La planta no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break
            



ejectutar_software()