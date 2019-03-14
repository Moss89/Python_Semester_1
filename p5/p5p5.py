# Take user input as a string
name = input("Please enter a town or city: ")

# Use if elif else statements to determine which province the town/city is in
if name == "Belfast" or name == "Derry" or name == "Lisburn":
    print("You entered " + name + ". " + name + " is in Ulster")

elif name == "Dublin" or name == "Kilkenny":
    print("You entered " + name + ". " + name + " is in Leinster")

elif name == "Limerick" or name == "Cork" or name == "Waterford":
    print("You entered " + name + ". " + name + " is in Munster")

elif name == "Galway" or name == "Sligo":
    print("You entered " + name + ". " + name + " is in Connacht")

# If no recognisable input is found, then display a sorry message
else:
    print("Sorry, I didn't recognise that name")





