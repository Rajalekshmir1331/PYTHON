class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def displayrectangle(self):
         print("the area is:",l*b)
         print("the perimeter is:",(2*(l+b)))
l=int(input("enter the length"))
b=int(input("enter the width"))
r1=rectangle(l,b)
r1.displayrectangle()
