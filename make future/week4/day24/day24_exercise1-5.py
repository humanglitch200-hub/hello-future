#exercise one:
a = (5)  #It's a list
b = (5,) #It's a tuple
print(a, b)

#unpacking variables:
details = ("prem", 20, "Nepal")
name, age, country = details
print(f"Name: {name}, Age: {age}, country: {country}")

#a functions that takes a list and returns (min, max, avg):
def stats(number):
    return min(number), max(number), sum(number)/ len(number)

values = [1,2,3,4,5,6,6,6,7,88]
low, high, average = stats(values)

print(low, high, average)


#Buiding a dict key:
city = {
    (12.1, -13.1): "kathmandu",
    (14.1, -15.2): "Pokhara",
    (16, -56.78): "nepaljung"
    }
try:
    lat =  float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))
    latitude = (lat, lon)
    search_city = city.get(latitude, "City not found!")
#I think word of get is siple :
#find key print its value!

    print(search_city)

except ValueError:
    print("Please enter valid number! ")
