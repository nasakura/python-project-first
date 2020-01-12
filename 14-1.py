#14-1
class Square:
  square_list= []
  def __init__(self):
    self.square_list.append(self)

  def show_list(self):
    print(self.square_list)

#Main
s1=Square()    
s2=Square()    
print(Square)
s1.show_list()
s2.show_list()
