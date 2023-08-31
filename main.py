import os
from tabulate import tabulate
from conexion import *
con = conectar()

def iniciar():
    os.system('clear')
    while True:
        print('Seleccione una de las opciones: ')
        print('\t1. Añadir un libro')
        print('\t2. Ver todos los libros')
        print('\t3. Buscar un libro')
        print('\t4. Modificar un libro')
        print('\t5. Eliminar un libro')
        print('\t6. Salir de la aplicación')
        opcion = input('Escoja una opción: ')

iniciar()