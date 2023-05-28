import sqlite3

conexion = sqlite3.connect('ejemplo.db')
c= conexion.cursor()

op= ('venta')
for row in c.execute('SELECT * FROM acciones WHERE operaciones = ? ', op):
    print (row)


conexion.close