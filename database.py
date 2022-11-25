import sqlite3 as sql


def signup(name, surname, age, email, password):
    connection = sql.connect('userdata.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)", [name, surname, age, email, password])
    connection.commit()
    connection.close()

