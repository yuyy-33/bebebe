import math

def calu_area_of_circle(radius):
    return math.pi* radius **2

radius = 5
area = calu_area_of_circle(radius)
print(f"The area of the circle with radius {radius}is:{area}")