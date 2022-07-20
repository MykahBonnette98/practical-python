#age calculator

# input needs int (number input) to divide age
#  line 12, decades needs str to print string output

age = int(input("How old are you?\n"))

decades = age // 10

years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old.")