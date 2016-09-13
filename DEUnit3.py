'''
Daryl Egan
Unit 2
'''

def kilo():
    kilometers = input("Enter a distance in kilometers: ")
    return kilometers
    
def miles(km):
    miles = float(km) * .6214            
    return miles

def out():
    print ("This program is going to convert kilometers to miles.")
    km = kilo()
    print ("The distance in miles is: ", round(miles(km),3))

out()



