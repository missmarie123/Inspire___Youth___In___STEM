#!/usr/bin/env python3
#This is a single line comment 
#python program to illustrate t
#name:Marie Wairimu
#email:mariewairimu01@gmail.com
#date:17th February 2023
#file:list_revisisted.py


#camel case
myFavouriteFruits = ["banana" , "apple" , "mango" , "lime" , "plums"]
for fruit in myFavouriteFruits:
    print(myFavouriteFruits)

#len is used to show the number of characters     
print(len(fruit))

friends = ["Phoebe" , "Joey" , "Chandler" , "Monica" , "Ross"]
print(friends)
friends [0] ="Moesha"
print(friends)


new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)

new_friends.clear()
print(new_friends)


