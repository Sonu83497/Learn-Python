# Duck Typing
class Duck:
    def walk(self):
        print("Thapak Thapak Thapak Thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")

class Cat:
    def walk(self):
        print("Meow Meow Meow Meow")

def myFunction(obj):
    obj.walk()
    
d = Duck()
myFunction(d)

h = Horse()
myFunction(h)

c = Cat()
myFunction(c)