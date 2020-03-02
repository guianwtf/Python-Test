print("Welcome to the Temperature Conversion Program \n")

temperature = float(input("What is the given temperature in degrees Farenheit: "))

FtoC = (temperature - 32) * 5/9
FtoK = (temperature +459.67) * 5/9


print("cyka blyat " + str(FtoK))

print(f"""
Degrees Fareneheit: {round(float(temperature),4)}
Degrees Celsius:    {round(float(FtoC),4)}
Degrees Kelvin:     {round(float(FtoK),4)}
""")