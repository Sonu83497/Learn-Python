import threading
t = threading.current_thread().getName()
print(t)

from threading import Thread
def disp(a,b):
    print("Thread Running :",a,b)
t = Thread(target=disp, args=(10,20))
t.start()

from threading import Thread
def disp(a,b):
    print("Thread Running :",a,b)
for i in range(5):
    t = Thread(target=disp, args=(10,20))
    t.start()

#impoting Thread class from threading module

from threading import Thread
def disp():
    print("Thread Running")
#Creating Thread Class object
t = Thread(target=disp)
#Starting Thread
t.start()    


#Importing Thread Class from threading Module
from threading import Thread
def disp(a,b):
    print("Threading Running :",a,b)
#creating thread class object
t = Thread(target=disp, args=(10,20))
#Starting Thread
t.start()

#Creating a thread by creating a child class to Thread Class 
#importing Thread class from threading module
from threading import Thread
class Mythread(Thread):
    pass
t = Mythread()
print(t.name)

#run()
from threading import Thread
class Mythread(Thread):
    def run(self):
        print("Run Method")
t = Mythread()
t.start()

#Creating a thread by creating a child class to thread class
#importing thread class from threading module
from threading import Thread
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")
            t = Mythread()
t.start()
t.join()
for i in range(5):
    print("Main Thread")
