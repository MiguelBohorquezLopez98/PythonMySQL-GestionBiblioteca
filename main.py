import os
from tabulate import tabulate
from conexion import *
from libro import *
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
        if opcion == '1':
            nuevo_libro()
        elif opcion == '2':
            ver_libros()
        elif opcion == '3':
            buscar_libro()
        elif opcion == '6':
            break
        else:
            print('Escoja una opción correcta')

def nuevo_libro():
    titulo = input('Ingrese el título del libro: ')
    autor = input('Ingrese el nombre del autor: ')
    estado = 'Disponible'
    respuesta = registrar(titulo, autor, estado)
    print(respuesta)

def ver_libros():
    datos = mostrar()
    headers = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def buscar_libro():
    id = input('Ingrese el id del libro: ')
    datos = buscar(id)
    headers = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

iniciar()