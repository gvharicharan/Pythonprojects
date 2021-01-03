#Product
class Product:
    def __init__(self):
        self.name='Redmi7'
        self.description='Its awesome'
        self.price=9000

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

p1=Product()
p1.display()

print(p1.name)
print(p1.description)
print(p1.price)
