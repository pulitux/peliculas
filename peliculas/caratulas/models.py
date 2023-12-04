from django.db import models
import cx_Oracle


class Pelicula:
    def __init__(self):
        self.connection = cx_Oracle.connect(user = 'system', password = 'pythonoracle', dsn = 'localhost/xe')
    def get_caratulas(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select titulo, foto from peliculas order by titulo")
        except self.connection.Error as e:
            print(e)
        return cursor
