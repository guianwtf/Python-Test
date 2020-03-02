print("Welcome to the Multriplicaiton/Exponent Table App")

name = input("What is your name? ").title().strip()
number = float(input("What number would like you like to work with? "))

print(f"Multiplication Table for: {number}\n")

for count in range(1,10):
    output = count * number
    print(f"""\t\t\t{count} * {number} = {round((output),2)}""")

print(f"Exponent Table for: {number}\n")

for count in range(1,10):
    output = number ** count
    print(f"""\t\t\t{count} * {number} = {round((output),4)}""")

print(f"""
     {name}
        {name.lower()}
            {name.title()}
                {name.upper()}
""")

exit()