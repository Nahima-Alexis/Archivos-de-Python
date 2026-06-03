entradas_disponibles = 50
entradas_vendidas = 0

while True:
    print("====== Sistema de Entradas para un Concierto ======")
    print("\n======================= MENU ======================")
    print("1.- Ver entradas Disponibles")
    print("2.- Comprar Entradas")    
    print("3.- Devolver Entradas")
    print("4.- Ver Entradas Vendidas")
    print("5.- Salir")
    
    try:
        opcion = int(input("\nIngrese una opcion: "))
        if opcion == 1:
            print(f"Entradas disponibles {entradas_disponibles}")
            
        elif opcion == 2:
            if entradas_disponibles > 0:
                try:
                    compras = int(input("Ingrese cantidad de entradas a comprar: "))
                    if compras <= 0:
                        print("La cantidad ingresada debe ser mayor a 0.")
                    elif compras > entradas_disponibles:
                        print("No hay suficientes entradas disponibles.")
                    else:
                        entradas_disponibles -= compras
                        entradas_vendidas += compras
                except ValueError:
                    print("ERROR! Debe ingresar SOLO numeros enteros.")
            else:
                print(f"Tenemos {entradas_disponibles} entradas disponibles, por lo tanto no se puede vender.")
                
        elif opcion == 3:
            if entradas_vendidas > 0:
                try:
                    devolucion_entradas = int(input("Ingrese la cantidad de entradas a devolver: "))
        
                    if devolucion_entradas <= 0:
                        print("Debe ingresar un valor positivo y mayor a 0.")
                        
                        #print("No se puede devolver entradas, ya que no se han comprado.")
                    elif devolucion_entradas > 50:
                        print("No puede superar el máximo de entradas del concierto (50).")
                    else:
                        entradas_disponibles += devolucion_entradas
                        entradas_vendidas -= devolucion_entradas
                        print(f"{devolucion_entradas} entradas devueltas con exito. ")
                except ValueError:
                    print("Error. Debe ingresar SOLO numeros enteros")
            else:
                print(f"Tenemos {entradas_vendidas} entradas vendidas, por lo tanto no puede devolver.")            
        elif opcion == 4:
            print(f"Entradas Vendidas {entradas_vendidas}")
            
        elif opcion == 5:
            print("Gracias por utilizar el sistema de Entradas para Concierto")
            break
        else:
            print("Por favor ingrese una opcion valida.")
    except ValueError:
        print("ERROR! Solo debe ingresar NUMEROS ENTEROS POSITIVOS.")
                