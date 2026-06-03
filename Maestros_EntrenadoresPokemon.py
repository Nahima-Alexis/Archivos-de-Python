#Pseudocódigo de Sistema de Registro de Entrenadores Pokémon
import os
os.system("cls")

maestros = 0
novatos = 0
print("=================================================")
print("================== BIENVENIDO/A =================")
print("=================================================")
print("\nSistema de Registro de Entrenadores Pokémon")
#1 Solicitar la cantidad de entrenadores y debe ser un numero entero positivo mayor que 0
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de entrenadores: "))
        if cantidad <= 0:
            print("Cantidad inválida. Debe ingresar un entero positivo.")
        else:
            break    
    except ValueError:
        print("Debe ingresar un numero entero positivo o mayor que 0.")
        
    #2 Solicitar el nombre de entrenador y debe ser igual o mayor que 6 caracteres y sin espacio
    # Usar ciclo de repeticion for
for i in range (cantidad):
    print("\nEntrenador", i + 1)    
    while True:
        nombre = input("Por favor ingresa tu nombre: ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("\nNombre inválido. Intente nuevamente.")
            
    #3 Solicitar cantidad de medallas obtenidas y debe ser un numero positivo
    #4 Clasificarlos según las medallas obtenidas        
    while True:
        try:
            medallas = int(input("Ingresa cantidad de medallas: "))
            if medallas < 0:
                print("Por favor ingresa solo numeros enteros POSITIVOS.")
                
            #5 Si es mayor a 8 es un maestro pokemon
            #6 Si es igual o menor que 8 es entrenador novato
            elif medallas > 8:
                print("Eres un maestro pokemon.")
                break
            elif medallas <= 8:
                print("Eres un entrenador novato.")
                break
            else:
                print("Cantidad inválida. Debe ingresar un entero positivo")
        except ValueError:
            print("Debe ingresar un numero entero positivo o mayor que 0.")
    
    #7 Un contador para contar el total de los maestros pokemon y un total de los entrenadores novatos
    if medallas > 8:
        maestros += 1 
    elif medallas <= 8:
        novatos += 1
#8 Al final debo mostrar en pantalla la cantidad de maestros pokemon y entrenadores novatos que se registraron        
print(f"\nSe registraron {maestros} Maestro(s) Pokémon y {novatos} Entrenador(es) Novato(s).")
              
        

    
