#14-3

class SelfCalss:
  def is_same_class(self ,c1 , c2):
    return c1 is c2


#Main

s1 = SelfCalss()
s2 = SelfCalss()

print(s1.is_same_class(s1,s1))
print(s1.is_same_class(s1,s2))
print(s2.is_same_class(s2,s2))
print(s2.is_same_class(s1,s2))
