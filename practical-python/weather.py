# Weather functions 
# If statments

#ex: 1
temp = 95

if temp > 80:    
    print("It's too hot!")
    print("Stay inside!")



#ex: 2 (temp is less < 60, prints its too cold/stay inside)
temp = 50

if temp > 80:    
    print("It's too hot!")
    print("Stay inside!")
elif temp < 60:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")        



#ex: 3 (is false, prints enjoy the outdoors)
temp = 75 
if temp > 80 or temp < 60:
    print("stay inside!")
else:
    print("Enjoy the outdoors!")    



#ex: 4 (is false, prints stay inside)
temp = 75
forecast = "rain"

if temp < 80 and forecast != "rain":
    print("Go outside!")
else:
    print("Stay inside!")


#ex: 5 ("not" means make oppisite,prints stay inside)
forecast = "rain"
if not forecast == "rain":
    print("Go outside!")
else:
    print("Stay inside!")
