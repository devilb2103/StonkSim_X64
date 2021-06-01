import multiprocessing
from time import sleep

class funcClass():

    def worker(self, text):
        while True:
            print(str(text))
            sleep(1)

if __name__ == '__main__':

    processList = {}

    for i in range(2):
        p = multiprocessing.Process(target=funcClass.worker, args=(funcClass, f"lol{i}",))
        p.start()
        processList[f"lmao123{i}"] = p
    sleep(10)
    print(processList.values())
    for k, p in processList.items():
        if(k.startswith("lmao123")):
            p.terminate()