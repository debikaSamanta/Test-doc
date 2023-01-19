from threading import Thread, Event
from time import sleep
from couchdb import Server


s = Server('http://admin:1234@localhost:5984/')
db = s['test']
    # the since parameter defaults to 'last_seq' when using continuous feed

#event = Event()

def fun1():
    ch = db.changes(feed='continuous',heartbeat='1000',include_docs=True)
    for line in ch:
        doc = line['doc']
        if(str(doc).__contains__("'author': 'Bob'")) :
            print(doc)
    sleep(3)

def fun2():
    while True:
        print("\n setEnv\n readRecord\n readData\n getAllRecords\n ")
        function = input()
        match function:
            case "setEnv":
                print('1 pressed')
            case "readRecord":
                print('readRecord')
            case "readData":
                print('readData')
            case "getAllRecords":
                print('getAllRecords')    
            case default:
                print('Bavda....Sala...')
        #event.set()
        sleep(1)


t = Thread(target=fun1)
s = Thread(target=fun2)
t.start()
s.start()
t.join()
s.join()

# import threading

# def get_input():
#     data = input() # Something akin to this
#     return data
