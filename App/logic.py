import time
import os 
import csv
import math
from DataStructures import array_list as al
from DataStructures import single_linked_list as sll
from DataStructures.Map import map_linear_probing as mlb
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

    al.selection_sort(filtrados, cmp_pickup_datetime)

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


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


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


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


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
