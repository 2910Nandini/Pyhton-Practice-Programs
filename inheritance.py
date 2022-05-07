#basic inheritance in python

class A:
    def random(self):
        print("i am in class A")

class B:
    def random(self):
        print("i am in class B")

item1=B()
item1.random()
item2=A()
item2.random()
