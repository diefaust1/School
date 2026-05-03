import threading
import time


def download_file():
    print("Download started...")

    for i in range(5):
        time.sleep(1)  # Simulates waiting for network/data
        print(f"Downloaded {20 * (i + 1)}%")

    print("Download finished!")

download_thread = threading.Thread(target=download_file)

download_thread.start()

for i in range(5):
    print("Main program is still running...")
    time.sleep(0.5)

download_thread.join()

print("Program finished.")