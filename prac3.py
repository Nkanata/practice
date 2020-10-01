from math import pi


def main():
    print("This program computes a volume and area of a sphere. ")
    print("Enter the radius of the sphere")

    radius = eval(input("Radius: "))
    volume = 4 / 3 * pi * radius * radius * radius
    print("the volume is : ", volume)

    area = 4 * pi * radius * radius
    print("The area is : ", area)


main()