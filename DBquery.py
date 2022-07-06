import psycopg2
from psycopg2 import Error


class DB():
    """
    Class for DB connect
    """

    @staticmethod
    def db_connect(userdb, passworddb, hostdb, portdb,
                   databasedb):
        try:
            connection = psycopg2.connect(user=userdb,
                                          password=passworddb,
                                          host=hostdb,
                                          port=portdb,
                                          database=databasedb)
            cursor = connection.cursor()
            return connection, cursor
        except (Exception, Error) as e:
            print("Error PostgreSQL", e)
            return None, None

    @staticmethod
    def db_close(cursor, connection):
        if connection:
            cursor.close()
            connection.close()
            print("ALL OK\nPostgreSQL connection close")