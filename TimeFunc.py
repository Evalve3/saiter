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
