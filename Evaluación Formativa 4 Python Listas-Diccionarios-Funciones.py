turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
}

def menu():
    print("         *** MENU PRINCIPAL ***          ")
    print("1.- Turistas por país.")
    print("2.- Turistas por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir")

def turistas_por_pais(pais):
    
    encontrado = False
    
    for turista in turistas:
        if pais == turistas[turista][1]:
            print(turistas[turista][0])
            encontrado = True
            
    if encontrado == False:
        print("No hay turistas de ese pais.")

def turistas_por_mes(mes):
    turistas_mensual = 0
    for turista in turistas:
        if mes == int(turistas[turista][2].split("-")[1]):
            turistas_mensual += 1
    porcentaje = (turistas_mensual / len(turistas)) * 100
    print(f"El porcentaje de turistas en el mes {mes} es: {porcentaje:.2f}%")
    return porcentaje
        

def eliminar_turista():
    pass

while True:
    menu()
    try:
        opcion = int(input("\nElige una opcion: "))
        
        if opcion == 1:
            pais = input("Ingresa el pais\n>>> ")
            turistas_por_pais(pais)
            
        elif opcion == 2:
            mes = int(input("Ingresa el mes\n>>> "))
            turistas_por_mes(mes)
            
        elif opcion == 3:
            eliminar_turista()
            
        elif opcion == 4:
            print("Saliendo...")
            break
    except ValueError:
        print("ERROR! SOLO DEBES INGRESAR NUMEROS ENTEROS.")