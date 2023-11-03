import rectarea
from math import pi
l=int(input("enter the length of the rectangle:"))
b=int(input("enter the width of the rectangle:"))
r=int(input("enter the radius of the cirlce:"))
print("rectangle area:",rectarea.rectarea(l,b));
print("rectangle perimeter:",rectarea.rectperi(l,b));
print("area of the circle:",rectarea.circlearea(r,pi));
print("circle perimeter:",rectarea.circleperi(pi,r));
