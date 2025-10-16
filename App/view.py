import sys
from App import logic as l
from DataStructures import array_list as al

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    catalog = l.new_logic()
    return catalog

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename = input("Ingrese el nombre del archivo: ")
    _,tiempo,total,menor_dist,mayor_dist,primeros,ultimos = l.load_data(control, filename)
    return _,tiempo,total,menor_dist,mayor_dist,primeros,ultimos


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    id = input("Ingrese el indice del dato a consultar: ")
    print(l.get_data(control, id))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    fecha_inicial = input("Ingrese la fecha inicial (AAAA-MM-DD HH:MM:SS ejemplo: 2015-01-15 07:00:00): ")
    fecha_final = input("Ingrese la fecha final (AAAA-MM-DD HH:MM:SS ejemplo: 2015-01-15 09:00:00): ")
    n = int(input("Ingrese la cantidad de viajes a mostrar (n): "))
    
    print("\n--- Resultado Requerimiento 1 ---")
    resultado = l.req_1(control, fecha_inicial, fecha_final, n)
    
    tiempo_ms = al.get_element(resultado, 0)['tiempo_ms']
    total_trayectos = al.get_element(resultado, 1)['total_trayectos']
    primeros = al.get_element(resultado, 2)['primeros']
    ultimos = al.get_element(resultado, 3)['ultimos']
    
    print(f"\nTiempo de ejecución: {tiempo_ms} ms")
    print(f"Total de trayectos encontrados: {total_trayectos}\n")
    
    if total_trayectos < 2*n:
        print("=" * 80)
        print("TOTAL {} TRAYECTOS:".format(al.size(primeros)))
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
        
    else:
        
        print("=" * 80)
        print("PRIMEROS {} TRAYECTOS:".format(al.size(primeros)))
        print("=" * 80)
    
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    
        print("\n" + "=" * 80)
        print("ÚLTIMOS {} TRAYECTOS:".format(al.size(ultimos)))
        print("=" * 80)
    
        for i in range(al.size(ultimos)):
            viaje = al.get_element(ultimos, i)
            numero_trayecto = total_trayectos - al.size(ultimos) + i + 1
            print(f"\nTrayecto #{numero_trayecto}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    print("\n")
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    lat_inicial = float(input("Ingrese la latitud inicial (00.00 ejemplo: 38.9): "))
    lat_final = float(input("Ingrese la latitud final (00.00 ejemplo: 40.10): "))
    n = int(input("Ingrese la cantidad de viajes a mostrar (n): "))
    
    print("\n--- Resultado Requerimiento 2 ---")
    resultado = l.req_2(control, lat_inicial, lat_final, n)
    
    tiempo_ms = al.get_element(resultado, 0)['tiempo_ms']
    total_trayectos = al.get_element(resultado, 1)['total_trayectos']
    primeros = al.get_element(resultado, 2)['primeros']
    ultimos = al.get_element(resultado, 3)['ultimos']

    print(f"\nTiempo de ejecución: {tiempo_ms} ms")
    print(f"Total de trayectos encontrados: {total_trayectos}\n")
    
    if total_trayectos < 2*n:
        print("=" * 80)
        print("TOTAL {} TRAYECTOS:".format(al.size(primeros)))
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
        
    else:
        
        print("=" * 80)
        print("PRIMEROS {} TRAYECTOS:".format(al.size(primeros)))
        print("=" * 80)
    
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    
        print("\n" + "=" * 80)
        print("ÚLTIMOS {} TRAYECTOS:".format(al.size(ultimos)))
        print("=" * 80)
    
        for i in range(al.size(ultimos)):
            viaje = al.get_element(ultimos, i)
            numero_trayecto = total_trayectos - al.size(ultimos) + i + 1
            print(f"\nTrayecto #{numero_trayecto}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    print("\n")
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    dist_inicial = float(input("Ingrese la distancia mínima (en millas): "))
    dist_final = float(input("Ingrese la distancia máxima (en millas): "))
    n = int(input("Ingrese la cantidad de viajes a mostrar (n): "))
    
    print("\n--- Resultado Requerimiento 3 ---")
    resultado = l.req_3(control, dist_inicial, dist_final, n)
    
    tiempo_ms = al.get_element(resultado, 0)['tiempo_ms']
    total_trayectos = al.get_element(resultado, 1)['total_trayectos']
    primeros = al.get_element(resultado, 2)['primeros']
    ultimos = al.get_element(resultado, 3)['ultimos']

    print(f"\nTiempo de ejecución: {tiempo_ms} ms")
    print(f"Total de trayectos encontrados: {total_trayectos}\n")
    
    if total_trayectos < 2*n:
        print("=" * 80)
        print("TOTAL {} TRAYECTOS:".format(al.size(primeros)))
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
        
    else:
        
        print("=" * 80)
        print("PRIMEROS {} TRAYECTOS:".format(al.size(primeros)))
        print("=" * 80)
    
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    
        print("\n" + "=" * 80)
        print("ÚLTIMOS {} TRAYECTOS:".format(al.size(ultimos)))
        print("=" * 80)
    
        for i in range(al.size(ultimos)):
            viaje = al.get_element(ultimos, i)
            numero_trayecto = total_trayectos - al.size(ultimos) + i + 1
            print(f"\nTrayecto #{numero_trayecto}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    print("\n")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    fecha = input("Ingrese la fecha de terminación (AAAA-MM-DD): ")
    momento = input("Ingrese el momento ('antes' o 'despues'): ")
    hora = input("Ingrese la hora de referencia (HH:MM:SS): ")
    n = int(input("Ingrese la cantidad de viajes a mostrar (n): "))
    
    print("\n--- Resultado Requerimiento 4 ---")
    resultado = l.req_4(control, fecha, momento, hora, n)
    
    tiempo_ms = al.get_element(resultado, 0)['tiempo_ms']
    total_trayectos = al.get_element(resultado, 1)['total_trayectos']
    primeros = al.get_element(resultado, 2)['primeros']
    ultimos = al.get_element(resultado, 3)['ultimos']

    print(f"\nTiempo de ejecución: {tiempo_ms} ms")
    print(f"Total de trayectos encontrados: {total_trayectos}\n")
    
    if total_trayectos < 2*n:
        print("=" * 80)
        print("TOTAL {} TRAYECTOS:".format(al.size(primeros)))
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
        
    else:
        
        print("=" * 80)
        print("PRIMEROS {} TRAYECTOS:".format(al.size(primeros)))
        print("=" * 80)
    
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    
        print("\n" + "=" * 80)
        print("ÚLTIMOS {} TRAYECTOS:".format(al.size(ultimos)))
        print("=" * 80)
    
        for i in range(al.size(ultimos)):
            viaje = al.get_element(ultimos, i)
            numero_trayecto = total_trayectos - al.size(ultimos) + i + 1
            print(f"\nTrayecto #{numero_trayecto}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    print("\n")



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    fecha_hora_terminacion = (input("Ingrese la fecha y hora de terminacion a consultar ( (formato “%Y-%m-%d %H” ej.: 2015-01-15 08): "))
    n = int(input("Ingrese la cantidad de viajes a mostrar (n): "))
    
    print("\n--- Resultado Requerimiento 5 ---")
    resultado = l.req_5(control, fecha_hora_terminacion, n)
    
    tiempo_ms = al.get_element(resultado, 0)['tiempo_ms']
    total_trayectos = al.get_element(resultado, 1)['total_trayectos']
    primeros = al.get_element(resultado, 2)['primeros']
    ultimos = al.get_element(resultado, 3)['ultimos']

    print(f"\nTiempo de ejecución: {tiempo_ms} ms")
    print(f"Total de trayectos encontrados: {total_trayectos}\n")
    
    if total_trayectos < 2*n:
        print("=" * 80)
        print("TOTAL {} TRAYECTOS:".format(al.size(primeros)))
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
        
    else:
        
        print("=" * 80)
        print("PRIMEROS {} TRAYECTOS:".format(al.size(primeros)))
        print("=" * 80)
    
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    
        print("\n" + "=" * 80)
        print("ÚLTIMOS {} TRAYECTOS:".format(al.size(ultimos)))
        print("=" * 80)
    
        for i in range(al.size(ultimos)):
            viaje = al.get_element(ultimos, i)
            numero_trayecto = total_trayectos - al.size(ultimos) + i + 1
            print(f"\nTrayecto #{numero_trayecto}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    print("\n")

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    barrio_recogida = (input("Ingrese el barrio de recogida: "))
    hora_inicial = (input("Ingrese la hora inicial(formato HH ej.:09): "))
    hora_final = (input("Ingrese la hora final(formato HH ej.:19): "))
    n = int(input("Ingrese la cantidad de viajes a mostrar (n): "))
    
    print("\n--- Resultado Requerimiento 6 ---")
    resultado = l.req_6(control, barrio_recogida, hora_inicial, hora_final, n)
    
    tiempo_ms = al.get_element(resultado, 0)['tiempo_ms']
    total_trayectos = al.get_element(resultado, 1)['total_trayectos']
    primeros = al.get_element(resultado, 2)['primeros']
    ultimos = al.get_element(resultado, 3)['ultimos']

    print(f"\nTiempo de ejecución: {tiempo_ms} ms")
    print(f"Total de trayectos encontrados: {total_trayectos}\n")
    
    if total_trayectos < 2*n:
        print("=" * 80)
        print("TOTAL {} TRAYECTOS:".format(al.size(primeros)))
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
        
    else:
        
        print("=" * 80)
        print("PRIMEROS {} TRAYECTOS:".format(al.size(primeros)))
        print("=" * 80)
    
        for i in range(al.size(primeros)):
            viaje = al.get_element(primeros, i)
            print(f"\nTrayecto #{i + 1}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    
        print("\n" + "=" * 80)
        print("ÚLTIMOS {} TRAYECTOS:".format(al.size(ultimos)))
        print("=" * 80)
    
        for i in range(al.size(ultimos)):
            viaje = al.get_element(ultimos, i)
            numero_trayecto = total_trayectos - al.size(ultimos) + i + 1
            print(f"\nTrayecto #{numero_trayecto}:")
            print(f"  Recogida: {viaje['pickup_datetime']}")
            print(f"  Coordenadas recogida: {viaje['pickup_coords']}")
            print(f"  Entrega: {viaje['dropoff_datetime']}")
            print(f"  Coordenadas entrega: {viaje['dropoff_coords']}")
            print(f"  Distancia: {viaje['trip_distance']} millas")
            print(f"  Costo total: ${viaje['total_amount']}")
    print("\n")

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            _,tiempo,total,menor_dist,mayor_dist,primeros,ultimos = load_data(control)
            print("Tiempo de carga (ms): " + str(tiempo))
            print('Total de trayectos: ' + str(total))
            print("\nTrayecto de menor distancia (distancia > 0.0 millas):")
            print(f"  - Fecha/Hora de inicio: {menor_dist['inicio']}")
            print(f"  - Distancia (millas): {menor_dist['distancia_millas']}")
            print(f"  - Costo total (USD): {menor_dist['costo_total']}")
            print("\nTrayecto de mayor distancia:")
            print(f"  - Fecha/Hora de inicio: {mayor_dist['inicio']}")
            print(f"  - Distancia (millas): {mayor_dist['distancia_millas']}")
            print(f"  - Costo total (USD): {mayor_dist['costo_total']}")
            print("\nPrimeros cinco trayectos cargados:")
            for idx, t in enumerate(primeros, start=1):
                print(f"  #{idx}")
                print(f"    • Inicio: {t['inicio']}")
                print(f"    • Fin: {t['fin']}")
                print(f"    • Duración (min): {t['duracion_min']}")
                print(f"    • Distancia (millas): {t['distancia_millas']}")
                print(f"    • Costo total (USD): {t['costo_total']}")
            print("\nÚltimos cinco trayectos cargados:")
            for idx, t in enumerate(ultimos, start=1):
                print(f"  #{idx}")
                print(f"    • Inicio: {t['inicio']}")
                print(f"    • Fin: {t['fin']}")
                print(f"    • Duración (min): {t['duracion_min']}")
                print(f"    • Distancia (millas): {t['distancia_millas']}")
                print(f"    • Costo total (USD): {t['costo_total']}")
                
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
