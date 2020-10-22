class Shoes:
  __privateVariable1 = "Open Toed"
  __privateVariable2 = "Close Toed"

  def __init__(self, nameValue, ageValue):
    self.name = nameValue
    self.age = ageValue

  def getprivateVariable1(self):
    return self.__privateVariable1

  def getprivateVariable2(self):
    return self.__privateVariable2

  def setprivateVariable1(self, value):
    self.__privateVariable1 = value

  def setprivateVariable2(self, value):
    self.__privateVariable2 = value

