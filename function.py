# determine function type
import math

def calculate():
    function = input("Would you like to calculate: \n area of a circle \n total due \n degrees celsius\n")

#area of circle
    if function == "area of a circle":
        radius = float(input("Please enter radius of the circle: \n"))
        def area():
            areaCalc = (radius ** 2) * math.pi
            return round(areaCalc, 2)
        return area()
#total due
    elif function == "total due":
        price = float(input("Please enter price: \n"))
        tax = float(input("Please enter tax: \n"))
        def total():
            totalCalc = price * (tax / 100) + price
            return round(totalCalc, 2)
        return total()
#degrees celsius
    elif function == "degrees celsius":
        fdeg = float(input("Please enter temperature in Fahrenheit: \n"))
        def cdeg():
            cdegCalc = (fdeg - 32) * (5 / 9)
            return round(cdegCalc, 5)
        return cdeg()
    else:
        return "Invalid Input"

result = calculate()
print(result)
