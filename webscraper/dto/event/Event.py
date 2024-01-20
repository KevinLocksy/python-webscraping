class Event:
  def __init__(self):
    self.initialize("","","","","","","","","","")

  def initialize(self,name,type,date,time,address,price,link,association,food,people):
    self.name=name
    self.type=type
    self.date=date
    self.time=time
    self.address=address
    self.price=price
    self.link=link
    self.association=association
    self.food=food
    self.people=people


  def setName(self,name): name=name
  def getName(self): return self.name
  def setType(self,type): self.type=type
  def getType(self): return self.type
  def setDate(self,date): self.date=date
  def getDate(self): return self.date
  def setTime(self,time): self.time=time
  def getTime(self): return self.time
  def setAddress(self,address): self.address=address
  def getAddress(self): return self.address
  def setPrice(self,price): self.price=price
  def getPrice(self): return self.price
  def setLink(self,link): self.link=link
  def getLink(self): return self.link
  def setAssociation(self,association): self.association=association
  def getAssociation(self): return self.association
  def setFood(self,food): self.food=food
  def getFood(self): return self.food
  def setPeople(self,people): self.people=people
  def getPeople(self): return self.people

  def __str__(self):
     return "Event:[name:"+self.name+",type:"+self.type+",date:"+self.date+",time:"+self.time+",address:"+self.address+",price:"+self.price+",link:"+self.link+",association:"+self.association+",food:"+self.food+",people:"+self.people+"]"

