class car: 
    def __init__(self,model,make,year,engine_capacity):
        self.model = model
        self.make = make
        self.year = year 
        self.engine_capacity = engine_capacity


#getters
    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year
    
    def get_engine_capacity(self):
        return self.engine_capacity

#setters - set the attributes
    def set_model(self,model):
        self.model = model

    def set_make(self,make):
        self.make = make

    def set_year(self,year):
        self.year = year


car_1 = car("demio","nissan",2018,1400)
car_2 =car("hilux","toyota",2020,350000)
car_3 =car("passat","vw",2009,2600)


car_1.set_year(2022)

print(car_1.get_model())
print(car_1.get_make())
print(car_1.get_year())
print(car_1.get_engine_capacity())

print(car_2.get_model())
print(car_2.get_make())
print(car_2.get_year())
print(car_2.get_engine_capacity())

print(car_3.get_model())
print(car_3.get_make())
print(car_3.get_year())
print(car_3.get_engine_capacity())

