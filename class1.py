#implementing classes and objects

class car:
    def __init__(self,b_name,model,types):
        self.b_name=b_name
        self.model=model
        self.types=types

car1=car("Maruti","Ciaz","Sedan")
print(car1.b_name)
print(car1.model)
print(car1.types)
