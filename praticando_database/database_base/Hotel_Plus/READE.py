import sqlite3

conn = sqlite3.connect("HotelPLus.db")
curso = conn.cursor()

# LENDO VALORES
curso.execute(
    ''' 
        SELECT * FROM usuario
    '''
)
usuarios = curso.fetchall()

for user in usuarios :
    print(user)

conn.close()