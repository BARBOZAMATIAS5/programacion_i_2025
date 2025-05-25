from funciones_auxiliares import *

def crear_matriz(y: int = 2, x: int = 2) -> list:
    '''
    Crea una matriz segun las filas y columnas pasadas por parametro
    Parametros: fila -> int, columna -> int 
    Return: retorna la lista creada
    '''
    matriz_creada = []
    for f in range(y):
        filas = []
        for c in range (x):
            filas.append([])
        matriz_creada.append(filas)

    return matriz_creada

def mostrar_matriz(matriz: list) -> None:
    '''
    Muestra por consola la matriz pasada por parametro
    Parametros: matriz -> list
    Return: no retorna nada
    '''
    for fila in matriz:
        print(fila)

def crear_matriz_personalizada() -> list:
    '''
    Crea una matriz personalizada dependiendo de los enteros 
    ingresados
    Parametro: ninguno
    Return: retorna la lista personalizada
    '''
    fila = ingresar_numero("Ingrese el numero de filas: ")
    columna = ingresar_numero("Ingrese el numero de columnas: ")

    return crear_matriz(fila, columna)

def editar_valores_matriz(matriz: list) -> list:
    '''
    
    
    
    '''
    matriz_modificada = matriz

    for i in range(len(matriz_modificada)):
        for j in range(len(matriz_modificada[i])):
            matriz_modificada[i][j] = ingresar_numero(f"Ingrese un valor para modificar fila {i+1} - columna {j+1}: ")

    return matriz_modificada