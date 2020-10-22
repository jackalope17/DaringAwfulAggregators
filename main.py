from Classes.Shoes_class import Shoes
from Labs import Labs

if True:
  labs = Labs()
  #labs.runlab2_1_1_7()
  #labs.runlab2_1_1_19()
  labs.runlab2_1_1_20()

if False:
  Sclass = Shoes('kane', 25)
  print(Sclass.name, Sclass.age)
  Sclass.name = 'Quincy'
  Sclass.age = 75
  print(Sclass.age, Sclass.name)

  Pclass = Shoes('kane', 25)
  print('\n----------------')
  print('Secret Files:')
  print('----------------')

  print('\n''Code Words:')
  print(Pclass.getprivateVariable1())
  print(Pclass.getprivateVariable2())

  print('\nReturn Code Words:')
  Pclass.setprivateVariable1('Flip-Flop')
  Pclass.setprivateVariable2('Tennis Shoes')

  print(Pclass.getprivateVariable1())
  print(Pclass.getprivateVariable2())

from vehicles.Vehicle import Vehicle
from vehicles.Landvehicle import Landvehicle
from vehicles.Seavehicle import Seavehicle
from vehicles.Airvehicle import Airvehicle
from vehicles.Spacevehicle import Spacevehicle
from vehicles.Wheeledvehicle import Wheeledvehicle
from vehicles.Trackedvehicle import Trackedvehicle
from vehicles.Hovercraftvehicle import Hovercraftvehicle
from vehicles.Car import Car
from vehicles.Truck import Truck

if False:
  vehicle = Vehicle()
  landV = Landvehicle()
  seaV = Seavehicle()
  airV = Airvehicle()
  spaceV = Spacevehicle()
  wheeledV = Wheeledvehicle()
  trackedV = Trackedvehicle()
  hcV = Hovercraftvehicle()
  car = Car()
  truck = Truck()

  vehicle.blowhorn()
  landV.blowhorn()
  wheeledV.blowhorn()
  seaV.blowhorn()
  airV.blowhorn()
  spaceV.blowhorn()
  trackedV.blowhorn()
  hcV.blowhorn()
  car.blowhorn()
  truck.blowhorn()

  print('')
  print(isinstance(car, Vehicle))
  print(isinstance(car, Seavehicle))
  print(issubclass(Hovercraftvehicle, Vehicle))
  print(issubclass(Wheeledvehicle, Spacevehicle))

