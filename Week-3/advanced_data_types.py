#Advanced data types

#mutable vs Immutable

#Mutable are data types that can be edited during program life cycle.You can add or remove elements

#Immutable are data types that cannot be edited during program life cycle

#1) - list(mutable)

friends = ["Melody" , "Joy" , "Chelsea" , "Emily"]
# or friends = [] for empty lists
students = ["Melissa" , "Miley" , "Bailey"]
friends.extend(students)
print(friends)
friends.append("Kelly")
print(friends)


#2 - tuples(immutable)
#Type of lists that are immutable
stationeries = ("ruler", "stapler","sticky notes" , "washi tape")

#replace the whole tuple
stationery = ("pen", "clip board" , "eraser")
for stationary in stationeries:
    print(stationary)

numbers = (1,2,3,4,5,6,7,8)
print(numbers)

#3 - dictonaries

#uses key and value pair
student = {"Name":"Marie","age":22,"gender" :" female"}
#"name" : Marie  -->name(key)   Marie(value)
print(student["Name"])
print(student["age"])
print(student["gender"])

#fav colour, hobby , course ,weight , height 
friend = {"Name":"Kelly" , "Favourite_colour" : "Black" , "Course" : "Financial engineering" , "Weight" : 65  , "Height" : 162 , "Hobby"  : "reading novels" }
print(friend["Name"])
print(friend["Favourite_colour"])
print(friend["Course"])
print(friend["Weight"])
print(friend["Height"])
print(friend["Hobby"])

print(student.values())
print(student.keys())

print(friend.keys())
print(friend.values())



#4 - sets
