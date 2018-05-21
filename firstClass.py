class CountFromBy(object):
    def __init__(self,v:int=0,i:int=1)->None:
        self.val = v
        self.incr = i
    def increase(self)->None:
        self.val += self.incr
    def __repr__(self)->str:
        return str(self.val)

c = CountFromBy(1,2)
c.increase()
print(c)