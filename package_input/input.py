def get_int (mensaje:str,minimo:int,maximo:int,error:str)->int:
    numero = int(input(mensaje))
    while numero >maximo or numero < minimo:
        numero = int(input(error))
    return numero

def get_float(mensaje: str, minimo: float, maximo: float, error: str) -> float:
    numero = float(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = float(input(error))
    return numero

def get_str(mensaje):
    respuesta = input(mensaje)
    return respuesta