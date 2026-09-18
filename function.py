# determine function type
import math

def calculate():
    function = input("Would you like to calculate: \n area of a circle \n total due \n degrees celsius\n")

#area of circle
    if function == "area of a circle":
        radius = float(input("Please enter radius of the circle: \n"))
        area = (radius ** 2) * math.pi
        area = round(area, 2)
        return area

#total due
    elif function == "total due":
        price = float(input("Please enter price: \n"))
        tax = float(input("Please enter tax: \n"))
        total = price * (tax / 100) + price
        total = round(total, 2)
        return total
#degrees celsius
    elif function == "degrees celsius":
        fdeg = float(input("Please enter temperature in Fahrenheit: \n"))
        cdeg = (fdeg - 32) * (5 / 9)
        cdeg = round(cdeg, 5)
        return cdeg
    else:
        return "Invalid Input"

result = calculate()
print(result)
