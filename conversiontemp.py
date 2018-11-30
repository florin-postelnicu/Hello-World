'''
conversion from Celsius  to Fahrenheit
C*9/5 +32 = F

conversion from Fahrenheit to Celsius

(F - 32)* 5/9 = C
'''


def conversion(degree, temp):
    if degree == 'f':
        C = (temp -32)*5/9
        print(temp, "F converted in C is :", round(C))
    elif degree =='c':
        F = temp*9/5 + 32
        print(temp, "C converted in F is :",round(F))

    else :
        print("There is no such type of degree: ", degree)


print('Input the type ')
deg = input("Enter c for Celsius, or f for Fahrenheit:  ")

temperature = int(input("Enter the value for temperature: "))
conversion (deg, temperature)
