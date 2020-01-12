#18-1
class Rectangle:
  def calculate_perimeter(self,width,height):
    return (width+height)*2
    

class Square:
  def calculate_perimeter(self,width):
    return width*4

#Main

r = Rectangle()
print("Rectangle : " + str(r.calculate_perimeter(10,20))) 
s = Square()
print("Square : " + str(s.calculate_perimeter(10))) 
