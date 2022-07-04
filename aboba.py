import urllib.request
import requests
import time


class Timer:
    def __init__(self, func):
        a = time.time()
        func()
        self.tm = time.time() - a


def check1():
    try:
        print("check1 start")
        requests.head("https://asdf-vm.com")
        print("Sucesfull")
    except BaseException as govno:
        print(govno)


def check2():
    try:
        print("check2 start")
        urllib.request.urlopen("https://asdf-vm.com")
        print("Sucesfull")
    except BaseException as govno:
        print(govno)


def who_winner(c1=0, c2=0, c1_sum=0, c2_sum=0):
    for i in range(20000):
        a = Timer(check1).tm
        c1_sum += a
        b = Timer(check2).tm
        c2_sum += b
        if a < b:
            c1 += 1
        else:
            c2 += 1

    print("check 1 time wins =", c1, "\ncheck 2 time wins", c2)
    print("check 1 sum tine =", c1_sum, "\ncheck 2 sum time=", c2_sum)


if __name__ == '__main__':
    who_winner()
