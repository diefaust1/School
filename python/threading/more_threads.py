import threading
import time


def task(name, seconds):
    print(f"{name} gestartet")

    for i in range(seconds):
        time.sleep(1)
        print(f"{name}: {i + 1} Sekunden vergangen")

    print(f"{name} beendet")


thread1 = threading.Thread(target=task, args=("Aufgabe 1", 3))
thread2 = threading.Thread(target=task, args=("Aufgabe 2", 5))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Alle Aufgaben beendet.")