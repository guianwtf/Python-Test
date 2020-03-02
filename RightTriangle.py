import math

print("Welcome to the Right Triangle Solver App \n")

first_leg = float(input("What is the first leg of the triangle: "))
second_leg = float(input("What is the second leg of the triangle: "))


hypotenuse = first_leg**2 + second_leg**2
area = (first_leg * second_leg) / 1/2
output = round(math.sqrt(hypotenuse), 3)

print(f"""
For a triangle with legs of {first_leg} and {second_leg} the hypotenuse is {output}.
For a triangle with legs of {first_leg} and {second_leg} the area is {area}
""")

#print(f"first {first_leg**2} ||| second {second_leg**2} ||| hypo{hypotenuse} || {output} || {area}")









