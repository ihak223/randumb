import datetime
import random
import time
import threading

def gahsgah():
    class Spinner:
        spinner = ["-", "\\", "|", "/", "-", "\\"]
        def __init__(self, start):
            self.start = start
            print(self.start)
        def update(self):
            print(self.spinner[self.start], end="\r")
            if self.start == len(self.spinner)-1:
                self.start = 0
            else:
                self.start += 1

    def r():
        today = datetime.datetime.now()

        a = random.randint(1, 16)
        # print(f"Generated : {a}")
        b = str(today.second)+str(a)+str(random.choice(["1", "54", "3"]))
        # print(f"Generated : {b}")
        c = [1]
        i = 0

        while i < random.randint(1, 10000000):
            # print(c[i])
            c.append(random.randint(1, 1567)%today.hour)
            i += 1

        d = b+str(today.microsecond)
        # print(f"Generated : {d}")
        e = int((int(d)+random.choice(c))/today.year+random.choice(c))
        # print(f"Generated : {e}")
        return e

    loading_thing = Spinner(0)
    j = []
    def rr():
        k = 0
        l = random.randint(0, 100)
    
        print(f"[{threading.current_thread().name}] Looping Randomly For : {l}.", end="\r")
        print("", end="\r")
        while k < l:
            o = r()%random.randint(1, k+20)
            # print()
            j.append(o)
            if k%5 == 1:
                loading_thing.update()
            k += 1
    # print(j)
    

    y = 0

    print(f"[{threading.current_thread().name}] Constructing Threads ... ")
    threads = random.randint(64, 128)
    while y < threads:
        t = threading.Thread(target=rr)
        t.start()
        t.join()
    
        y += 1
    print("                                                 ", end="\r")
    print("Finished Threads :)", end="\r")   
    print()


    total = 0
    for number in j:
        oper = random.randint(0, 3)
        if oper == 0:
            total += number
        elif oper == 1:
            total -= number
        elif oper == 2:
            total += total*number
        else:
            total *= number
    print(total)
