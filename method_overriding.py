class parent:
    def f(self):
        print("the f method in parent class")
class child(parent):
    def f (self):
        print("the f method in child class")
obj1=child()
obj1.f()
