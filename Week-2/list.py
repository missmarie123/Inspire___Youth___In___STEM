names = ["Marie" , "Kelly" , "Val" , "Cece", "Euny"]
#accesing items in a list
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])
print(names[1:3])
fruits = ["grapes" , "apples" , "mangoes" , "plums" , "guava" , "bananas" , "pinapples"]
print(fruits[0:])
print(fruits[3])
print("my favourite fruit is",fruits[0])
print("my favourite fruit is",fruits[0].upper())
#adding two lists
vegetables = ["kales" , "carrot" , "cabbage" , "spinach" , "managu" , "onion"]
stationary = ["pens" , "ink" , "paper" , "glue" , "scissors" , "stapler"]
shoppings = vegetables + stationary
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings: 
    print(shopping)
print("My name is  "  + names[0] +" " + "and my favourite fruit is  " + fruits[0] )




