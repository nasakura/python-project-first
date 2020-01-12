#13-4

class Rider:
  def __init__(self,rider_name):
    self.name = rider_name
#    print("Set Rider Name :" + self.name)
 

#  def __init__(self):
#    pass

  def rider_name(self):
#    print("return Rider Name :  " + self.name)
    return self.name

class Horse:
  def __init__(self,horse_name,rider):
    self.horse_name = horse_name 
    self.rider =  rider

#  def __init__(self,rider_info):
#    self.rider =  rider_info
    
  def show_rider(self):
#    print("騎手:" + self.rider.rider_name())
    print("馬名:" + self.horse_name + ",騎手:" + self.rider.rider_name())

#Main


h = Horse("シンボリルドルフ",Rider("岡部幸雄"))
h.show_rider()
