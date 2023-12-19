import sqlite3

def create_table():
    conn = sqlite3.connect('ranking.db')
    cursor = conn.cursor()
    try:
        sentencia = '''
        CREATE TABLE IF NOT EXISTS ranking(
            player_name TEXT,
            score INTEGER
        )
        '''

        cursor.execute(sentencia)
    except sqlite3.OperationalError as error:
        print(f"No se pudo crear la tabla. Detalles:\n{error}")

    
def insert_values(player_name, score):
    with sqlite3.connect("ranking.db") as connection:
        try:
            connection.execute("INSERT INTO ranking (player_name,score) values(?,?)", (player_name, score))
            connection.commit
        except Exception as error:
            print(f"Error al insertar campos. Detalles: {error}")
    
def get_table():
    with sqlite3.connect("ranking.db") as connection:
        exect = connection.execute("SELECT * FROM ranking ORDER BY score DESC LIMIT 4")
        rows = exect.fetchall()

        return rows