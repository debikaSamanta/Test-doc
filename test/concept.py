import sys
import time
import threading
from queue import Queue


class Actor(threading.Thread):

    def __init__(self):
        super().__init__(target=self.run)
        self.queue = Queue()

    def send(self, msg):
        self.queue.put(msg)
        print(f"sent: {msg}")  # DEBUG

    # def close(self):
    #     print()  # DEBUG
    #     self.send('STOP')

    def run(self):
        for msg in iter(self.queue.get, 'STOP'):
            pass


class PrintActor(Actor):
    def run(self):
        for msg in iter(self.queue.get, 'STOP'):
            print(f"got: {msg}")  # DEBUG


if __name__ == '__main__':

    pa = PrintActor()
    pa.start()
    pa.send("Hello")
    pa.send("debika")
    pa.send("samanta")
    pa.send("Done.....!")
    #time.sleep(1)
    pa.send("...World!")
    time.sleep(2)
    pa.join()