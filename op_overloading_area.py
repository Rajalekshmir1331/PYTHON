class  rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __lt__(self,other):
        return self.area()<other.area()
    def area(self):
        return self.length*self.width
r1=rectangle(2,3)
r2=rectangle(5,3)
if (r1<r2):
    print("r1 is less than r2");
