from pathlib import Path

import pandas as pd
import psycopg2
import sqlalchemy
from sqlalchemy.engine.base import Connection

import Photo


class BancoDeDados:

    connection: Connection

    def __init__(self) -> None:
        self.connection = self.getEngine().connect()

    # user, password, host, port, database
    def getStringConexao(self):
        # engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/dvdrental')
        string_conexao = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            'postgres', 'mysecretpassword', 'localhost', '5432', 'dvdrental')
        print(string_conexao)
        return string_conexao

    def getConnection(self):
        return self.getEngine().connect()

    def getEngine(self):
        return sqlalchemy.create_engine(self.getStringConexao())

    def consultaPandas(self):
        df = pd.read_sql_table('actor', self.getEngine(),
                               columns=["first_name", "last_name"])
        print(df.head())

    def consultaSQL(self):
        df = pd.read_sql_query("select * from actor", self.getEngine())
        print(df.head())

        query = '''
        SELECT  act.first_name,
                act.last_name,
                film.title
        FROM actor act
        INNER JOIN film_actor film_actor
        ON act.actor_id = film_actor.actor_id
        INNER JOIN film film
        ON film.film_id = film.film_id;
        '''

        df = pd.read_sql_query(query, self.getEngine())
        print(df.head())

    def inserir(self):
        # Create connection
        conn = self.getConnection()

        # Begin transaction
        trans = conn.begin()

        conn.execute(
            "INSERT INTO actor (first_name, last_name, last_update) VALUES ('Alan', 'Padua', '2013-01-01')")
        trans.commit()

        # Close connection
        conn.close()

    def criarTabelaPhotos(self):
        conn = self.getConnection()
        trans = conn.begin()

        conn.execute(
            "CREATE TABLE public.Python_Employee (id INT NOT NULL , name TEXT NOT NULL , photo bytea NOT NULL , PRIMARY KEY (id))")

        trans.commit()
        conn.close()

    def inserirPhotos(self, photo: Photo):
        conn = self.getConnection()
        trans = conn.begin()

        sql_insert_blob_query = """ INSERT INTO public.python_employee (id, name, photo) VALUES (%s,%s,%s)"""

        # Convert data into tuple format
        insert_blob_tuple = (photo.id, photo.name, photo.file)

        conn.execute(sql_insert_blob_query, insert_blob_tuple)

        trans.commit()
        conn.close()

    def removerPhotos(self):
        conn = self.getConnection()
        trans = conn.begin()

        sql_insert_blob_query = """ DELETE FROM public.python_employee """

        conn.execute(sql_insert_blob_query)

        trans.commit()
        conn.close()

# banco = BancoDeDados()
# banco.criarTabelaPhotos()
