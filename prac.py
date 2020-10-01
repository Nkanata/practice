def main():
    print("This is Temperature Converter from Celsius to Fahrenheit")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")


main()
