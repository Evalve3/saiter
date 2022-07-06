import urllib.request
import psycopg2
from psycopg2 import Error
from itertools import permutations
from string import ascii_lowercase
import signal

class TimeoutException(Exception):
    def __init__(self, *args, **kwargs):
        pass


def signal_handler():
    raise TimeoutException()


def time_break(func):
    """
    Декоратор, останавливающий работу декорируемой функции, если её
    выполнение, заняло более 10 секунд
    """

    def wrapper(*args, **kwargs):
        try:
            # print("Запускаем тестируемую функцию")
            signal.signal(signal.SIGALRM, signal_handler)
            signal.alarm(5)
            res = func(*args, **kwargs)
            signal.alarm(0)
            # print("Нормальное завершение")
            return res
        except TimeoutException:
            pass
            # print("Time out")
        except:
            pass
            # print("Some other exception")

    return wrapper


@time_break
def check_site(url):
    try:
        urllib.request.urlopen(url)
        return url
    except:
        return None


def add_site_com(cursor, connection, url_for_check):
    url_for_check = 'https://' + url_for_check + '.com'
    url = check_site(url_for_check)
    if url:
        pgs_query = f'''
                            INSERT INTO sites_com (url)
                            VALUES
                            ('{url}');
                '''
        cursor.execute(pgs_query)
        connection.commit()
        print("site add")


if __name__ == '__main__':

    try:
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="123",
                                      host="localhost",
                                      port="5432",
                                      database="Sites")
        cursor = connection.cursor()
        a = set(permutations(ascii_lowercase, 2))
        for i in a:
            tmp = ''
            for j in i:
                tmp += j
            print(tmp)
            add_site_com(cursor, connection, tmp)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
