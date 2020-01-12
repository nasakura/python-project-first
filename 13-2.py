#18-2
class Rectangle:
  def calculate_perimeter(self,width,height):
    return (width+height)*2
    

class Square:
  def __init__(self,width):
    self.width = width


  def calculate_perimeter(self,width):
    return width*4


  def calculate_perimeter(self):
    return self.width*4

  def change_size(self,width_index):
    self.width += width_index

#Main
s = Square(10)
print("Square 10 : " + str(s.calculate_perimeter()))
s.change_size(10)
print("Square Add 10 : " + str(s.calculate_perimeter()))
s.change_size(-15)
print("Square Add 20-15 : " + str(s.calculate_perimeter()))
