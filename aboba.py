import urllib.request
import psycopg2
from psycopg2 import Error
from itertools import permutations
from string import ascii_lowercase
import signal


class TimeoutException(Exception):
    """
    Exception Timeout
    """

    def __init__(self, *args, **kwargs):
        pass


class TimeFunc():
    """
    Timer for function work
    """

    @staticmethod
    def __signal_handler():
        """
        raise TimeoutException
        """

        raise TimeoutException()

    @staticmethod
    def time_break(func):
        """
        Decorator, stop function, if decoration function work more 5 sec
        """

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, TimeFunc.__signal_handler)
                signal.alarm(5)
                res = func(*args, **kwargs)
                signal.alarm(0)
                return res
            except TimeoutException:
                pass
                # print("Time out")
            except:
                pass
                # print("Some other exception")

        return wrapper


class SiteAdder():
    """
    Incluede on DB site class
    """

    @TimeFunc.time_break
    @staticmethod
    def check_site(url):
        """
        Check open Site
        :param url: site url
        :return:Site url if site opening, else None
        """
        try:
            urllib.request.urlopen(url)
            return url
        except BaseException as e:
            return None

    @staticmethod
    def add_site(cursor, connection, url_for_check, prefix='https://', postfix='.com'):
        """
        Add site on your db if Site opening
        :param cursor: cursos for sql query
        :param connection: db connection
        :param url_for_check:
        :param prefix:
        :param postfix:
        :return:
        """
        url_for_check = prefix + url_for_check + postfix
        url = SiteAdder.check_site(url_for_check)
        if url:
            pgs_query = f'''
                                INSERT INTO sites_com (url)
                                VALUES
                                ('{url}');
                    '''
            cursor.execute(pgs_query)
            connection.commit()
            print("site add")


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


def main():
    connection, cursor = DB.db_connect("postgres", "123", "localhost", "5432", "Sites")
    if (connection):
        a = set(permutations(ascii_lowercase, 2))
        for i in a:
            tmp = ''
            for j in i:
                tmp += j
            print(tmp)
            SiteAdder.add_site(cursor, connection, tmp)
    DB.db_close(cursor, connection)


if __name__ == '__main__':
    main()
