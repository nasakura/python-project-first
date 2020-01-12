#12-2 
import math

class Circle:
  def area(self,r):
    return math.pow(r,2)*math.pi

# main module
c = Circle()
print(c.area(10))
