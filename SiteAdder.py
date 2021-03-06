from TimeFunc import TimeFunc
import urllib.request


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
