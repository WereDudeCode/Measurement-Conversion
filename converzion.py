import sys, os, time, pyfiglet

# ASCII Title Card
ascii_banner = pyfiglet.figlet_format("Converzion")
print(ascii_banner)

#Intro
def intro():
    conversion = input("What would you like to convert?\n")
    if conversion == "inches":
        inches()
    elif conversion == "ounces":
        ounces()
    else:
        print("Your entry is not valid...")
        intro()

#Ounces Flow
def ounces():
    ounces = float(input("Enter your measurment in ounces.\n"))
    convert_to_pounds = round(ounces * .0625)
    print("Your measurment equals " + str(convert_to_pounds) + " pounds!")


#Inches Flow    
def inches():
    measurment = int(input("Enter your measurment in inches.\n"))
    if measurment < 12:
        print ("Please enter a number greater than or equal to 12 inches")
        inches()
    converted_measurment = measurment / 12
    
    print("Your measurment equals " + str(converted_measurment) + " feet!")

intro()
