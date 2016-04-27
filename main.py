#!/usr/bin/python3 
#~/.bashrc
from options import *
from imported_file_options import *

# possibly create list of headers to check if 
# Create initial options list 

options = """Option 1 - General Statistics for Each Trade Station
Option 2 - Statistics for Specific Trade Stations
Option 3 - All Statistics for Specific Items for All Trade Stations
Option 4 - Specific Statistics for Items Based on User Input
Option 5 - Input Your Own Data File
* type "Help" for extra tips and instructions
* type "Exit" to exit the program"""

# Loop through the initial set of options
status = True
print("""Welcome! This data analysis module contains 4 data files for the four main trade stations in Eve Online - Amarr, Jita, Dodixie, and Rens. 
Each data file contains most of the items you can trade along with their buy order and sell order statistics.
Enjoy!""")
while status:
    print(options)
    choice = input("Choose one of the options above: ")
    choice = str(choice)
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    elif choice == "4":
        option4()
    elif choice == "5":
        option5()
        going = True
        while going:
            print(options)
            choice = input("Choose one of the options above: ")
            if choice == "1":
                option1_2()
            elif choice == "2":
                option2_2()
            elif choice == "3":
                option3_2()
            elif choice == "4":
                option4_2()
            elif choice.lower() == "help":
                help_message()
            elif choice.lower() == "exit":
                print("Thank you for your time! Please come back for all your Eve Online data analysis needs!")
                status = False
            else:
                print("Error: Invalid input.")
                print()
                continue
    elif choice.lower() == "help":
        help_message()
    elif choice.lower() == "exit":
        print("Thank you for your time! Please come back for all your Eve Online data analysis needs!")
        status = False
    else:
        print("Error: Invalid input.")
        print()
        continue