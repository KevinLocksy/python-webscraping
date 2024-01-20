class Event:
  def __init__(self,url,type,name,date,location,price="unknown"):
    self.url = url
    self.type = type
    self.name = name
    self.date = parse(date)
    self.location = location
    self.price = price

  def parseDate(date):
    return date

  def __str__(self):
    return "Event:["+
     "[url:"+self.url+"],"+
     "[type:"+self.type+"],"+
     "[name:"+self.name+"],"+
     "[date:"+self.date+"],"+
     "[location:"+self.location+"],"+
     "[price:"+self.price+"]"+
     "]"