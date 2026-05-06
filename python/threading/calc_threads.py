import threading
import time, random



def getNumberList (list_length) -> list:

    r_numbers = []
    for i in range (list_length):
        r_numbers.append(random.randrange(1,20))

    return r_numbers

def do_math (numbers) -> float:

    sum = 0
    for i in numbers:
        sum = sum + i
    
    sum = sum * 5 * 2 + 10

    sum = sum / 2

    return sum

def task(name, seconds):
    print(f"{name} gestartet")

    for i in range(seconds):
        time.sleep(1)
        print(f"{name}: {i + 1} Sekunden vergangen")

    print(f"{name} beendet")

def calc():

    numbers = getNumberList(200000)

    #for i in numbers:
        #print(i)
    
    result = do_math(numbers)

    print(result)
    print("Math done")


thread1 = threading.Thread(target=task, args=("Download", 10))
thread2 = threading.Thread(target=calc, args=())

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Alle Aufgaben beendet.")