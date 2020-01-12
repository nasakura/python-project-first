#14-2
class Square:
  def __init__(self,width):
    self.width = width
    
  def __repr__(self):
    list = [str(self.width),str(self.width),str(self.width),str(self.width)]
    return " by ".join(list)

#Main

print(Square(29))
