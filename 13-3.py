#13-3
class Shape:
 def what_am_i(self):
   print("I am a shape")

class Rectangle(Shape):
  pass
  

class Square(Shape):
  pass



#Main
r = Rectangle()
s = Square()
r.what_am_i()
s.what_am_i()
