from itertools import permutations
from string import ascii_lowercase
from SiteAdder import SiteAdder
from DBquery import DB


def main():
    connection, cursor = DB.db_connect("postgres", "123", "localhost", "5432", "Sites")
    max_len = int(input("Input max site len\n"))
    if (connection):
        for i in range(2, max_len + 1):
            a = set(permutations(ascii_lowercase, i))
            for i in a:
                tmp = ''
                for j in i:
                    tmp += j
                print(tmp)
                SiteAdder.add_site(cursor, connection, tmp)
        DB.db_close(cursor, connection)


if __name__ == '__main__':
    main()
