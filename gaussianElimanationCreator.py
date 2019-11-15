import random

dimensions = int(input("Enter the amount of dimensions you want (integer format plz)"))
variables = []
coefficients = []
totals = []
equatStrings = []

#randomly choosing the values of the dimensions, e.g x,y,z in three dimensions
for i in range(dimensions):
    variables.append(random.randint(-5, 5)) #these are the bounds in which your variables to solve can occupy

#randomly choosing the coefficients to generate the equations
for i in range(dimensions):
    coefficients.append([])
    for j in range(dimensions):
        coefficients[i].append(random.randint(-3, 3)) #these are the bounds in which your coefficients to solve can occupy

#creating a string format for the equatuons for the user
for i in range(dimensions):
    tempEquat = ""
    for j in range(dimensions):
        tempEquat = tempEquat + str(coefficients[i][j]) + (chr(123 - dimensions + j)) #chr(120) is the ascii for x
        if j != dimensions - 1:
            tempEquat = tempEquat + " + "
        else:
            tempEquat = tempEquat + " = "
    equatStrings.append(tempEquat)

#calculating the the right hand side of the equations
for i in range(len(variables)):
    total = 0
    for j in range(len(coefficients)):
        total = total + variables[j] * coefficients[i][j]
    totals.append(total)

#adding the totals to the end of the strings
for i in range (len(equatStrings)):
    equatStrings[i] = equatStrings[i] + str(totals[i])

print(equatStrings)

input("press enter to see answers")

for i in range(len(variables)):
    print (chr(123 - dimensions + i) + " = " + str(variables[i]))

