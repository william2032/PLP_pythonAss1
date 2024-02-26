#store name,age,locaions of user 
name = str(input("Enter your name :"))
age = int(input("Enter your age :"))
location = str(input("Enter your location :"))

result = 'Hello {} you are {} years old and you live in {}.'.format(name ,age, location)

print(result)