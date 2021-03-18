print("Welcome! This is UC (unit converter) for converting Miles into Kilometers.")

while True:
    print("Please enter a number of miles for conversion into kilometers. Enter ONLY a number!")

    mi = input("Miles: ")
    mi = float(mi.replace(",", ".")) #replace comma with dot, if user enters a comma.

    km = mi * 1.609344

    print("{0} miles is {1} kilometers.".format (mi, km))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break
