# Unity Converter

print("-------- Welcome to the Unit Converter of kilometers into miles  --------")

miles = 0
kilometers = 0
multiplier_km_miles = 0.62137119
repeat_loop = True
response = None

while repeat_loop == True:

    response_OK = ""
    kilometers = int(input("Please enter the number of kilometers: "))
    miles = kilometers * multiplier_km_miles
    print("The miles are: " + str(miles))

    while response_OK != "OK":

        response = input("Do you want to do another conversion? (Y/N): ")

        if response == "n" or response == "N":
            response_OK = "OK"
            repeat_loop = False
            print("Goodbye!")
        elif response == "y" or response == "Y":
            response_OK = "OK"
            repeat_loop = True
        else:
            response_OK = "NOK"
            repeat_loop = True


