import mysql.connector

conexion = mysql.connector.connect(user='Edgar', password='12345', database='oferta_academica')
cursor = conexion.cursor()

select = 'SELECT * from materia'
cursor.execute(select)
rows = cursor.fetchall()
materias = rows

for materia in materias:
    print(materia[1])
    select = 'SELECT * from seccion WHERE clave_materia = %s'
    cursor.execute(select, (materia[0],))
    rows = cursor.fetchall()
    secciones = rows
    for s in secciones:
        select = 'SELECT * from horario WHERE nrc_seccion = %s'
        cursor.execute(select, (s[0],))
        rows = cursor.fetchall()
        horarios = rows

        select = 'SELECT * from profesor WHERE id = %s'
        cursor.execute(select, (s[-1],))
        rows = cursor.fetchall()
        profesores = rows

        print(s, horarios, profesores)


