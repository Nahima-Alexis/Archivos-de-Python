# PSEUDOCODIGO - MAPA MENTAL
# 1. Mostrar menú con 4 rolls + opción para terminar pedido
# 2. Repetir (while True) hasta que el usuario termine su pedido (break)
# 3. Preguntar si tiene código de descuento (if/else)
#    3a. Si tiene código:
#        - Si es "soyotaku" → aplicar 10% de descuento
#        - Si no → mostrar "código no válido" 
#          y repetir (otro while) hasta que reingrese o escriba X
# 4. Mostrar detalle: cantidad de cada roll, subtotal, descuento y total final
# 5. Preguntar si desea otro pedido o salir
#-----------------------------------------------------------------------------------------------------------------------
import os
os.system("cls")

pikachu_roll = 0
otaku_roll = 0
pulpo_venenoso_roll = 0
anguila_electrica_roll = 0

precio_pikachu_roll = 4500
precio_otaku_roll = 5000
precio_pulpo_venenoso_roll = 5200
precio_anguila_electrica_roll = 4800

subtotal = 0
descuento = 0
total_final = 0

salir = False
while not salir:
    print(" ")
    print("=========== Tienda de Sushi ===========")
    print("Bienvenido a la tienda virtual de Sushi")
    print("------------------Menú-----------------")
    print(" ")
    print("1.- Pikachu Roll = $4.500")
    print("2.- Otaku Roll = $5.000")
    print("3.- Pulpo Venenoso Roll = $5.200")
    print("4.- Anguila Eléctrica = $4.800")
    print("5.- Finalizar compra")
    
    try:
        opcion = int(input("Por favor, ingresa una opción:\n--> "))
        
        if opcion == 1:
            pikachu_roll += 1
            print("Has elegido 'Pikachu Roll'")
        
        elif opcion == 2:
            otaku_roll += 1
            print("Has elegido 'Otaku Roll'")
            
        elif opcion == 3:
            pulpo_venenoso_roll += 1
            print("Has elegido 'Pulpo Venenoso Roll'")
            
        elif opcion == 4:
            anguila_electrica_roll += 1
            print("Has elegido 'Anguila Eléctrica Roll'")
            
        elif opcion == 5:
            print("Finalizando compra...")

            subtotal += precio_pikachu_roll * pikachu_roll
            subtotal += precio_otaku_roll * otaku_roll
            subtotal += precio_pulpo_venenoso_roll * pulpo_venenoso_roll
            subtotal += precio_anguila_electrica_roll * anguila_electrica_roll

            productos = pikachu_roll + otaku_roll + pulpo_venenoso_roll + anguila_electrica_roll

            while True:
                codigo_de_descuento = input("¿Tienes código de descuento?\nPara 'Si' escribe 's'\nPara 'No' escribe 'n'\n--> ").lower()
                if codigo_de_descuento == "s":
                    codigo_de_descuento = input("Por favor, ingresa el código de descuento\nAqui --> ").lower()
                    if codigo_de_descuento == "soyotaku":
                        descuento = int(subtotal * 0.10)
                        print("Se ha aplicado un 10% de descuento al total de tu compra.")
                        break
                    else:
                        print("Código no válido.")
                elif codigo_de_descuento == "n":
                    break
                else:
                    print("Código inválido.")
                    print("'R' Para volver a intentarlo\n'X' para volver al menu principal")
                    opcion = input("Elige una opcion: ").upper()
                    if opcion == "R":
                        continue
                    elif opcion == "X":
                        break

            total_final = subtotal - descuento
            print("*************************************************")
            print(f"        TOTAL PRODUCTOS: {productos}")          
            print("*************************************************") 
            print(f"Pikachu Roll: {pikachu_roll}")
            print(f"Otaku Roll: {otaku_roll}")              
            print(f"Pulpo Venenoso Roll: {pulpo_venenoso_roll}")
            print(f"Anguila Electrica Roll: {anguila_electrica_roll}")
            print("*************************************************")
            print(f"SubTotal por pagar: $ {subtotal}")
            print(f"Descuento por código: $ {descuento}")
            print(f"TOTAL: $ {total_final}")            
            print("\nGRACIAS POR TU COMPRA.")

            while True:
                print("\n¿Desea realizar otro pedido?\nPara confirmar presione '1'\nPara salir del programa presione '2'")
                try:
                    opcion = int(input("Ingresa tu opción: "))
                    if opcion == 1:
                        print("Volviendo al menu...")
                        subtotal = 0
                        descuento = 0
                        total_final = 0
                        pikachu_roll = 0
                        otaku_roll = 0
                        pulpo_venenoso_roll = 0
                        anguila_electrica_roll = 0
                        break
                    elif opcion == 2:
                        salir = True
                        break
                    else:
                        print("Opción no válida.")
                except ValueError:
                    print("ERROR! por favor ingresa un numero entero valido")
        else:
            print("Por favor, elige una opción válida dentro del menú.")
            
    except ValueError:
        print("¡ERROR! Por favor ingresa solo números enteros.")