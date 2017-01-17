class Car:
  
  speed = 0
  def __init__(self, name="General", model="GM", type="saloon"):
    self.name = name
    self.model = model
    self.type = type
    
    
    if self.name == "Porshe" or self.name == "Koenigsegg":
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
    
    if self.type=="trailer":
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
    
      
  def setSpeed(self, speed):
    self.speed = speed

  def is_saloon(self):
    if self.type != "trailer":
      self.type = "saloon"
      return True
      
  def drive(self, speed):
    if self.type != "trailer":
      self.setSpeed(1000)
    else:
      self.setSpeed(77)
    print(self)
    return self
      