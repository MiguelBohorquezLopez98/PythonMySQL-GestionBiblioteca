from conexion import *

def registrar(titulo, autor, estado):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = ''' INSERT INTO libro (titulo, autor, estado)
        values (%s, %s, %s)'''
        datos = (titulo, autor, estado)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Registro correcto'
    except mysql.Error as err:
        print('Ha ocurrido un error', err)

def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = "SELECT * FROM libro"
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
    except mysql.Error as err:
        print('Ha ocurrido un error', err)
    return datos

def buscar(id):
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = "SELECT * FROM libro WHERE id=%s"
        cursor.execute(sentencia_sql, (id,))
        datos = cursor.fetchall()
        con.close()
    except mysql.Error as err:
        print('Ha ocurrido un error', err)
    return datos