def validar_entero(n: input) -> bool:
    '''
    Verifica si lo ingresado es un entero
    Parametros: n -> input
    Return: un booleano
    '''
    if n.isdigit():
        return True
    else:
        return False
    
def castear_entero(n: input) -> int:
    '''
    Castea lo pasado por parametro a entero si es posible
    Paramentros: n -> input
    Retorna: un int (en lo posible, de lo contrario un mensaje por
                    consola para reintentar el ingreso)
    '''
    if validar_entero(n):
        return int(n)
    else:
        print("Error al ingresar el numero, intentelo nuevamente")
    
def ingresar_numero(mensaje: str) -> int:
    '''
    Pide al usuario ingresar un int, en caso que no sea, va a 
    solicitarlo nuevamente
    Parametros: ninguno
    Return: un int
    '''
    verificar = True

    while verificar:
        numero = castear_entero(input(mensaje))
        if type(numero) == int:
            verificar = False

    return numero