class car:
    def __init__(self,name,color,price,kilometer):
        self.name=name
        self.color=color
        self.price=price
        self.kilometer=kilometer
    def __len__(self):
        return self.kilometer
    def  __add__(self,other):
        return self.price + other.price
car1=car("swift","red",600000,4000)
car2=car("alto","black",300000,5000)
print(len(car1))
print(car1 + car2)
