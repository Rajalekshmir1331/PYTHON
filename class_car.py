class cars:
    def __init__ (self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def displaycars(self):
        print("name",self.name)
        print("price",self.price)
        print("color",self.color)
car1=cars("swift",640000,"red")
car2=cars("audi",2500000,"black")
car1.displaycars()
car2.displaycars()
