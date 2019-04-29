import glob
import json
import mysql.connector
import unicodedata

# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

conexion = mysql.connector.connect(user='Edgar', password='12345', database='oferta_academica')
cursor = conexion.cursor()

files = glob.glob('*.json')

def existe_carrera(seccion):
    select = 'SELECT * from carrera WHERE nombre = %s'
    cursor.execute(select, (seccion['carrera'],))

    rows = cursor.fetchall()
    if (len(rows) > 0):
        return True
    else:
        return False

def insertar_carrera(seccion):
    insert = 'INSERT INTO carrera(nombre) VALUES(%s)'
    cursor.execute(insert, (seccion['carrera'],))
    conexion.commit()
    return cursor.lastrowid

def existe_materia(seccion):
    select = 'SELECT * from materia WHERE clave = %s'
    cursor.execute(select, (seccion['clave'],))

    rows = cursor.fetchall()
    if (len(rows) > 0):
        return True
    else:
        return False

def insertar_materia(seccion):
    insert = 'INSERT INTO materia(clave, nombre, creditos) VALUES(%s, %s, %s)'
    cursor.execute(insert, (seccion['clave'], seccion['materia'], seccion['creditos']))
    conexion.commit()

def existe_carrera_materia(id_carrera, clave_materia):
    select = 'SELECT * from carrera_materia WHERE id_carrera = %s and clave_materia = %s'
    cursor.execute(select, (id_carrera, clave_materia))

    rows = cursor.fetchall()
    if (len(rows) > 0):
        return True
    else:
        return False

def inserta_carrera_materia(id_carrera, clave_materia):
    insert = 'INSERT INTO carrera_materia(id_carrera, clave_materia) VALUES(%s, %s)'
    cursor.execute(insert, (id_carrera, clave_materia))
    conexion.commit()

def existe_profesor(seccion):
    select = 'SELECT * from profesor WHERE nombre = %s'
    cursor.execute(select, (seccion['profesor'],))

    rows = cursor.fetchall()
    if (len(rows) > 0):
        return True
    else:
        return False

def insertar_profesor(seccion):
    insert = 'INSERT INTO profesor(nombre) VALUES(%s)'
    cursor.execute(insert, (seccion['profesor'],))
    conexion.commit()
    return cursor.lastrowid

def existe_periodo(seccion):
    select = 'SELECT * from periodo WHERE periodo = %s'
    cursor.execute(select, (seccion['periodo'],))

    rows = cursor.fetchall()
    if (len(rows) > 0):
        return True
    else:
        return False

def insertar_periodo(seccion):
    insert = 'INSERT INTO periodo(periodo) VALUES(%s)'
    cursor.execute(insert, (seccion['periodo'],))
    conexion.commit()
    return cursor.lastrowid

def existe_seccion(seccion):
    select = 'SELECT * from seccion WHERE nrc = %s'
    cursor.execute(select, (seccion['nrc'],))

    rows = cursor.fetchall()
    if (len(rows) > 0):
        return True
    else:
        return False

def insertar_seccion(seccion, id_periodo, id_profesor):
    insert = 'INSERT INTO seccion(nrc, seccion, cupos, disponibles, id_periodo, clave_materia, id_profesor)' \
             ' VALUES(%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert, (seccion['nrc'],
                            seccion['seccion'],
                            seccion['cupos'],
                            seccion['disponibles'],
                            id_periodo,
                            seccion['clave'],
                            id_profesor
                            ))
    conexion.commit()

def existe_horario(horario, nrc):
    select = 'SELECT * from horario WHERE hora = %s and dias = %s and edificio = %s and aula = %s and nrc_seccion = %s'
    cursor.execute(select, (horario['hora'],
                            horario['dias'],
                            horario['edificio'],
                            horario['aula'],
                            nrc
                            ))

    rows = cursor.fetchall()
    if (len(rows) > 0):
        return True
    else:
        return False

def insertar_horario(seccion, nrc_seccion, sesion):
    insert = 'INSERT INTO horario(sesion, hora, dias, edificio, aula, nrc_seccion)' \
             ' VALUES(%s, %s, %s, %s, %s, %s)'
    cursor.execute(insert, (sesion,
                            seccion['hora'],
                            seccion['dias'],
                            seccion['edificio'],
                            seccion['aula'],
                            nrc_seccion
                            ))
    conexion.commit()

def getID_carrera(carrera):
    select = 'SELECT id from carrera WHERE nombre = %s'
    cursor.execute(select, (carrera,))
    rows = cursor.fetchall()
    return rows[0][0]

def getID_profesor(profesor):
    select = 'SELECT id from profesor WHERE nombre = %s'
    cursor.execute(select, (profesor,))
    rows = cursor.fetchall()
    return rows[0][0]

def getID_periodo(periodo):
    select = 'SELECT id from periodo WHERE periodo = %s'
    cursor.execute(select, (periodo,))
    rows = cursor.fetchall()
    return rows[0][0]

for file in files:
    with open(file, encoding='utf-8') as f:
        oferta = json.load(f)
        for c in oferta:
            id_carrera = 0
            id_periodo = 0
            id_profesor = 0
            if not existe_carrera(c):
                id_carrera = insertar_carrera(c)
            else:
                id_carrera = getID_carrera(c['carrera'])
            if not existe_materia(c):
                insertar_materia(c)
            if not existe_carrera_materia(id_carrera, c['clave']):
                inserta_carrera_materia(id_carrera, c['clave'])
            if not existe_profesor(c):
                id_profesor = insertar_profesor(c)
            else:
                id_profesor = getID_profesor(c['profesor'])
            if not existe_periodo(c):
                id_periodo = insertar_periodo(c)
            else:
                id_periodo = getID_periodo(c['periodo'])
            if not existe_seccion(c):
                insertar_seccion(c, id_periodo, id_profesor)

            for horario in c['datos']:
                if not existe_horario(horario, c['nrc']):
                    insertar_horario(horario, c['nrc'], c['sesion'])
