print("Welcome! This is UC (unit converter) for converting Kilowatts into Horsepowers.")

while True:
    print("Please enter a number of kilowatts (kW) for conversion into horsepowers (hp). Enter ONLY a number!")

    kW = input("Kilowatts: ")
    kW = float(kW.replace(",", ".")) #replace comma with dot, if user enters a comma.

    hp = kW * 1.341022

    print("{0} kilowatts is {1} horsepowers.".format (kW, hp))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break

