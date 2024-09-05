#1 Variables and assignment

name = "Rockie"
age = 20
height = 5.11
favorite_color = "blue"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"hello: {name}, my favorite color is {favorite_color}!")
print("my age is {:d} and my height is {:.1f} feet.".format(age, height))

print(f"""
    name: {name} 
    age: {age}
    height: {height}
    favorite color: {favorite_color}
""")

radius = 5
circle_area = 3.14159 * (radius ** 2)
print(f"area of the circle: {circle_area:.1f}")

import math
sqrt_age = math.sqrt(age)
print(f"Square root of age: {sqrt_age:.2f}")

sine_height = math.sin(height)
cosine_height = math.cos(height)

print(f"sine of height: {sine_height:.2f}")
print(f"cosine of height: {cosine_height:.2f}")

#3 Expressions
sum_age = age + 5
difference_height = height - 4
product_age_height = age * height
quotient_height = height / 2
remainder_age = age % 3
age_power_2 = age ** 2

print(f"Sum of age and 5: {sum_age}")
print(f"Difference between height and 4: {difference_height:.1f}")
print(f"Product of age and height: {product_age_height:.1f}")
print(f"Quotient of height divided by 2: {quotient_height:.1f}")
print(f"Remainder of age divided by 3: {remainder_age}")
print(f"Age raised to the power of 2: {age_power_2}")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
