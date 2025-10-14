import time
import os 
import csv
import math
from DataStructures import array_list as al
from DataStructures import single_linked_list as sll
from DataStructures.Map import map_linear_probing as mlp    
from DataStructures.Map import map_separate_chaining as msc
from datetime import datetime

csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic(): 
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "taxis" : al.new_list(),
        "neighborhoods" : al.new_list(),
    }
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    inicio = get_time()   
    
    n_archivo = "Data/" + filename

    archivo = csv.DictReader(open(n_archivo, encoding='utf-8'))    

    for llave in archivo:

        llave["pickup_datetime"] = datetime.strptime(llave["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        llave["dropoff_datetime"] = datetime.strptime(llave["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
        llave["passenger_count"] = int(llave["passenger_count"])
        llave["trip_distance"] = float(llave["trip_distance"])
        llave["pickup_longitude"] = float(llave["pickup_longitude"])
        llave["pickup_latitude"] = float(llave["pickup_latitude"])
        llave["rate_code"] = int(llave["rate_code"])
        llave["dropoff_longitude"] = float(llave["dropoff_longitude"])
        llave["dropoff_latitude"] = float(llave["dropoff_latitude"])
        llave["payment_type"] = str(llave["payment_type"])
        llave["fare_amount"] = float(llave["fare_amount"])
        llave["extra"] = float(llave["extra"])
        llave["mta_tax"] = float(llave["mta_tax"])
        llave["tip_amount"] = float(llave["tip_amount"])
        llave["tolls_amount"] = float(llave["tolls_amount"])
        llave["improvement_surcharge"] = float(llave["improvement_surcharge"])
        llave["total_amount"] = float(llave["total_amount"])
        
        al.add_last(catalog["taxis"], llave)
        
    filename2 = "Data/nyc-neighborhoods.csv"
    
    archivo2 = csv.DictReader(open(filename2, encoding='utf-8'), delimiter=";")

    for llave2 in archivo2:
        llave2["borough"] = llave2["borough"]
        llave2["neighborhood"] = llave2["neighborhood"]
        lat_str = llave2["latitude"].replace(',', '.')
        lon_str = llave2["longitude"].replace(',', '.')
        llave2["latitude"] = float(lat_str)
        llave2["longitude"] = float(lon_str)

        al.add_last(catalog["neighborhoods"], llave2)

    tamanio = catalog["taxis"]["size"]
    
    i = 0
    
    min = al.get_element(catalog["taxis"], 0)

    max = min

    while min["trip_distance"] <= 0.0:
        i +=1
        min = al.get_element(catalog["taxis"], i)

    for valor in range(0, catalog["taxis"]["size"]):
        elem = al.get_element(catalog["taxis"], valor)
        if elem["trip_distance"] < min["trip_distance"] and elem["trip_distance"] > 0.0:
            min = elem
        elif elem["trip_distance"] > max["trip_distance"]:
            max = elem
    
    fmt = "%Y-%m-%d %H:%M:%S"
    mas_corto = {
        "inicio": min["pickup_datetime"].strftime(fmt),
        "distancia_millas": round(min["trip_distance"], 2),
        "costo_total": round(min["total_amount"], 2)
    }

    mas_largo = {
        "inicio": max["pickup_datetime"].strftime(fmt),
        "distancia_millas": round(max["trip_distance"], 2),
        "costo_total": round(max["total_amount"], 2)
    }
    primeros = []
    
    ultimos = []
    
    for i in range(0, 5):

        element = al.get_element(catalog["taxis"], i)

        resta = element["dropoff_datetime"] - element["pickup_datetime"]
        minutos = resta.total_seconds()/60

        info = {
            "inicio": element["pickup_datetime"].strftime(fmt),
            "fin": element["dropoff_datetime"].strftime(fmt),
            "duracion_min": minutos,
            "distancia_millas": round(element["trip_distance"], 2),
            "costo_total": round(element["total_amount"], 2)
        }
        primeros.append(info)

    for i in range(tamanio-5, tamanio):
        elemento = al.get_element(catalog["taxis"], i)
        
        resta = elemento["dropoff_datetime"] - elemento["pickup_datetime"]
        minutos = resta.total_seconds()/60
        
        info = {
            "inicio": elemento["pickup_datetime"].strftime(fmt),
            "fin": elemento["dropoff_datetime"].strftime(fmt),
            "duracion_min": minutos,
            "distancia_millas": round(elemento["trip_distance"], 2),
            "costo_total": round(elemento["total_amount"], 2)
        }

        ultimos.append(info)

    
    final = get_time()
    tiempo = delta_time(inicio, final)
    
    retorno = catalog, tiempo, tamanio, mas_corto, mas_largo, primeros, ultimos
    
    return retorno
# Funciones de consulta sobre el catálogo


def req_1(catalog, f_inicial, f_final, n):
    
    inicio = get_time()
    
    fecha_inicial = datetime.strptime(f_inicial, "%Y-%m-%d %H:%M:%S")
    fecha_final = datetime.strptime(f_final, "%Y-%m-%d %H:%M:%S")

    taxis = catalog["taxis"]
    filtrados = al.new_list()
    
    for i in range(al.size(taxis)):
        registro = al.get_element(taxis, i)
        if fecha_inicial <= registro["pickup_datetime"] <= fecha_final:
            al.add_last(filtrados, registro)

    def cmp_pickup_datetime(trip1, trip2):
        return trip1["pickup_datetime"] < trip2["pickup_datetime"]

    filtrados = al.merge_sort(filtrados, cmp_pickup_datetime)

    total = al.size(filtrados)
    fmt = "%Y-%m-%d %H:%M:%S"

    primeros = al.new_list()
    ultimos = al.new_list()

    limite = min(n, total)

    for i in range(limite):
        elem = al.get_element(filtrados, i)
        info = {
            "pickup_datetime": elem["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(elem["pickup_latitude"], 5), round(elem["pickup_longitude"], 5)],
            "dropoff_datetime": elem["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(elem["dropoff_latitude"], 5), round(elem["dropoff_longitude"], 5)],
            "trip_distance": round(elem["trip_distance"], 2),
            "total_amount": round(elem["total_amount"], 2)
        }
        al.add_last(primeros, info)
        
    for i in range(total - limite, total):
        elem = al.get_element(filtrados, i)
        info = {
            "pickup_datetime": elem["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(elem["pickup_latitude"], 5), round(elem["pickup_longitude"], 5)],
            "dropoff_datetime": elem["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(elem["dropoff_latitude"], 5), round(elem["dropoff_longitude"], 5)],
            "trip_distance": round(elem["trip_distance"], 2),
            "total_amount": round(elem["total_amount"], 2)
        }
        al.add_last(ultimos, info)

    final = get_time()
    tiempo = delta_time(inicio, final)

    resultado = al.new_list()
    al.add_last(resultado, {"tiempo_ms": round(tiempo, 2)})
    al.add_last(resultado, {"total_trayectos": total})
    al.add_last(resultado, {"primeros": primeros})
    al.add_last(resultado, {"ultimos": ultimos})

    return resultado


def req_2(catalog, lat_inicial, lat_final, n):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    inicio = get_time()
    
    taxis = catalog["taxis"]
    filtrados_lat = al.new_list()
    
    # Filtrar trayectos dentro del rango de latitud
    for i in range(al.size(taxis)):
        registro = al.get_element(taxis, i)
        pickup_lat = float(registro["pickup_latitude"])
        if lat_inicial <= pickup_lat <= lat_final:
            al.add_last(filtrados_lat, registro)
            
    def cmp_pickup_lat(trip1, trip2):
        lat1 = float(trip1["pickup_latitude"])
        lat2 = float(trip2["pickup_latitude"])
        lon1 = float(trip1["pickup_longitude"])
        lon2 = float(trip2["pickup_longitude"])
        
        # Ordenar de mayor a menor latitud
        if lat1 != lat2:
            return lat1 > lat2
        # Si latitudes iguales, ordenar de mayor a menor longitud
        else:
            return lon1 > lon2
    
    filtrados_lat = al.merge_sort(filtrados_lat, cmp_pickup_lat)
    total = al.size(filtrados_lat)
    fmt = "%Y-%m-%d %H:%M:%S"
    
    primeros = al.new_list()
    ultimos = al.new_list()
    
    limite = min(n, total)
    
    for i in range(limite):
        elem = al.get_element(filtrados_lat, i)
        info = {
            "pickup_datetime": elem["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(elem["pickup_latitude"], 5), round(elem["pickup_longitude"], 5)],
            "dropoff_datetime": elem["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(elem["dropoff_latitude"], 5), round(elem["dropoff_longitude"], 5)],
            "trip_distance": round(elem["trip_distance"], 2),
            "total_amount": round(elem["total_amount"], 2)
        }
        al.add_last(primeros, info)
    
    for i in range(total - limite, total):
        elem = al.get_element(filtrados_lat, i)
        info = {
            "pickup_datetime": elem["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(elem["pickup_latitude"], 5), round(elem["pickup_longitude"], 5)],
            "dropoff_datetime": elem["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(elem["dropoff_latitude"], 5), round(elem["dropoff_longitude"], 5)],
            "trip_distance": round(elem["trip_distance"], 2),
            "total_amount": round(elem["total_amount"], 2)
        }
        al.add_last(ultimos, info)

    final = get_time()
    tiempo = delta_time(inicio, final)
    
    resultado = al.new_list()
    al.add_last(resultado, {"tiempo_ms": round(tiempo, 2)}) 
    al.add_last(resultado, {"total_trayectos": total})
    al.add_last(resultado, {"primeros": primeros})
    al.add_last(resultado, {"ultimos": ultimos})
    
    return resultado


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog, fecha_hora, n):
    
    inicio = get_time()

    taxis = catalog["taxis"]
    mapa_horas = mlp.new_map(num_elements=al.size(taxis), load_factor=0.7)

    for i in range(al.size(taxis)):
        registro = al.get_element(taxis, i)

        clave = registro["dropoff_datetime"].strftime("%Y-%m-%d %H")  
        lista = mlp.get(mapa_horas, clave)
        if lista is None:
            lista = al.new_list()
        al.add_last(lista, registro)
        mlp.put(mapa_horas, clave, lista)

    filtrados = mlp.get(mapa_horas, fecha_hora)

    if filtrados is None or al.size(filtrados) == 0:
        final = get_time()
        tiempo = delta_time(inicio, final)
        vacio = al.new_list()
        resultado = al.new_list()
        al.add_last(resultado, {"tiempo_ms": round(tiempo, 2)})
        al.add_last(resultado, {"total_trayectos": 0})
        al.add_last(resultado, {"primeros": vacio})
        al.add_last(resultado, {"ultimos": vacio})
        return resultado

    def cmp_dropoff_desc(trip1, trip2):
        return trip1["dropoff_datetime"] > trip2["dropoff_datetime"]

    filtrados = al.merge_sort(filtrados, cmp_dropoff_desc)

    total = al.size(filtrados)
    fmt = "%Y-%m-%d %H:%M:%S"
    primeros = al.new_list()
    ultimos = al.new_list()
    limite = min(n, total)

    for i in range(limite):
        elem = al.get_element(filtrados, i)
        info = {
            "pickup_datetime": elem["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(elem["pickup_latitude"], 5), round(elem["pickup_longitude"], 5)],
            "dropoff_datetime": elem["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(elem["dropoff_latitude"], 5), round(elem["dropoff_longitude"], 5)],
            "trip_distance": round(elem["trip_distance"], 2),
            "total_amount": round(elem["total_amount"], 2)
        }
        al.add_last(primeros, info)

    for i in range(total - limite, total):
        elem = al.get_element(filtrados, i)
        info = {
            "pickup_datetime": elem["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(elem["pickup_latitude"], 5), round(elem["pickup_longitude"], 5)],
            "dropoff_datetime": elem["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(elem["dropoff_latitude"], 5), round(elem["dropoff_longitude"], 5)],
            "trip_distance": round(elem["trip_distance"], 2),
            "total_amount": round(elem["total_amount"], 2)
        }
        al.add_last(ultimos, info)

    final = get_time()
    tiempo = delta_time(inicio, final)

    resultado = al.new_list()
    al.add_last(resultado, {"tiempo_ms": round(tiempo, 2)})
    al.add_last(resultado, {"total_trayectos": total})
    al.add_last(resultado, {"primeros": primeros})
    al.add_last(resultado, {"ultimos": ultimos})

    return resultado

def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0 # radio tierra (km)
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c

def req_6(catalog, nombre_barrio, hora_inicial_str, hora_final_str, n_muestra):
    
    inicio = get_time()

    num_barrios = al.size(catalog["neighborhoods"])
    mapa_barrios = mlp.new_map(num_elements=num_barrios, load_factor=0.7)

    taxis = catalog["taxis"]
    total_taxis = al.size(taxis)
    barrios = catalog["neighborhoods"]
    total_barrios = al.size(barrios)

    # Indexar los viajes por barrio
    # Para cada viaje, se determina a qué barrio pertenece su punto de recogida
    for i in range(total_taxis):
        viaje = al.get_element(taxis, i)
        pickup_lat = viaje["pickup_latitude"]
        pickup_lon = viaje["pickup_longitude"]

        # Buscar el barrio más cercano (menor distancia Haversine)
        barrio_encontrado = None
        distancia_minima = float('inf')
        
        for j in range(total_barrios):
            barrio = al.get_element(barrios, j)
            distancia = haversine(pickup_lat, pickup_lon, barrio["latitude"], barrio["longitude"])
            
            if distancia < distancia_minima:
                distancia_minima = distancia
                barrio_encontrado = barrio["neighborhood"]

        if barrio_encontrado is not None:
            lista_viajes = mlp.get(mapa_barrios, barrio_encontrado)
            if lista_viajes is None:
                lista_viajes = al.new_list()

            al.add_last(lista_viajes, viaje)
            mlp.put(mapa_barrios, barrio_encontrado, lista_viajes)

    # Obtener los viajes del barrio solicitado
    viajes_barrio = mlp.get(mapa_barrios, nombre_barrio)

    # Si el barrio no existe o no hay viajes registrados
    if viajes_barrio is None or al.size(viajes_barrio) == 0:
        final = get_time()
        resultado = al.new_list()
        al.add_last(resultado, {"tiempo_ms": round(tiempo, 2)}) 
        al.add_last(resultado, {"total_trayectos": 0})
        al.add_last(resultado, {"primeros": primeros})
        al.add_last(resultado, {"ultimos": ultimos})
        return resultado

    # Convertir horas a enteros
    hora_inicial = int(hora_inicial_str)
    hora_final = int(hora_final_str)

    # Filtrar viajes dentro del rango horario
    filtrados = al.new_list()
    total_viajes = al.size(viajes_barrio)

    for i in range(total_viajes):
        v = al.get_element(viajes_barrio, i)
        hora = v["pickup_datetime"].hour
        if hora_inicial <= hora < hora_final:
            al.add_last(filtrados, v)

    # Ordenar del más antiguo al más reciente
    def cmp_fecha_asc(a, b):
        return a["pickup_datetime"] < b["pickup_datetime"]

    filtrados = al.merge_sort(filtrados, cmp_fecha_asc)

    # Seleccionar primeros y últimos N
    total_filtrados = al.size(filtrados)
    limite = n_muestra if n_muestra < total_filtrados else total_filtrados
    primeros = al.new_list()
    ultimos = al.new_list()
    fmt = "%Y-%m-%d %H:%M:%S"

    # Primeros N
    for i in range(limite):
        v = al.get_element(filtrados, i)
        info = {
            "pickup_datetime": v["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(v["pickup_latitude"], 5), round(v["pickup_longitude"], 5)],
            "dropoff_datetime": v["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(v["dropoff_latitude"], 5), round(v["dropoff_longitude"], 5)],
            "trip_distance": round(v["trip_distance"], 2),
            "total_amount": round(v["total_amount"], 2)
        }
        al.add_last(primeros, info)

    # Últimos N
    for i in range(total_filtrados - limite, total_filtrados):
        v = al.get_element(filtrados, i)
        info = {
            "pickup_datetime": v["pickup_datetime"].strftime(fmt),
            "pickup_coords": [round(v["pickup_latitude"], 5), round(v["pickup_longitude"], 5)],
            "dropoff_datetime": v["dropoff_datetime"].strftime(fmt),
            "dropoff_coords": [round(v["dropoff_latitude"], 5), round(v["dropoff_longitude"], 5)],
            "trip_distance": round(v["trip_distance"], 2),
            "total_amount": round(v["total_amount"], 2)
        }
        al.add_last(ultimos, info)

    final = get_time()
    tiempo = delta_time(inicio, final)

    resultado = al.new_list()
    al.add_last(resultado, {"tiempo_ms": round(tiempo, 2)}) 
    al.add_last(resultado, {"total_trayectos": total_filtrados})
    al.add_last(resultado, {"primeros": primeros})
    al.add_last(resultado, {"ultimos": ultimos})
    
    return resultado


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
