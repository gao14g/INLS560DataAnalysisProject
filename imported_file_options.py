from dictionary_builder import *
from helpers import *
from options import *

def option5():
    options = """Option 1 - General Statistics for Each Trade Station
Option 2 - Statistics for Specific Trade Stations
Option 3 - All Statistics for Specific Items for All Trade Stations
Option 4 - Specific Statistics for Items Based on User Input
* type "Help" for extra tips and instructions
* type "Exit" to exit the program"""

    trade_stations_2 = """Option 1 - Amarr
Option 2 - Dodixie
Option 3 - Jita
Option 4 - Rens
Option 5 - User File
Option 6 - Go Back to the Main Menu"""

    # Define function for all option 1 functionalities
    def option1_2():
        list = ["1","2","3"]
        status = True
        while status:
            print (general_options)
            print()
            answer = input("Choose one of the options above: ")
            print()
            if answer == "1":
                print("Here are some general statistics about the data files")
                print("Amarr:")
                print("The Highest Buy Volume is:", max_stats(amarr_dict,"Buy Vol"))
                print("The Highest Buy Average is:", max_stats(amarr_dict,"Buy Avg"))
                print("The Highest Buy Max is:", max_stats(amarr_dict,"Buy Max"))
                print("The Highest Buy Min is:", max_stats(amarr_dict,"Buy Min"))
                print("The Highest Buy Standard Deviation is:", max_stats(amarr_dict,"Buy StdDev"))
                print("The Highest Buy Median is:", max_stats(amarr_dict,"Buy Median"))
                print("The Highest Buy Percentile is:", max_stats(amarr_dict,"Buy Percentile"))
                print("The Highest Sell Vol is:", max_stats(amarr_dict,"Sell Vol"))
                print("The Highest Sell Average is:", max_stats(amarr_dict,"Sell Avg"))
                print("The Highest Sell Max is:", max_stats(amarr_dict,"Sell Max"))
                print("The Highest Sell Min is:", max_stats(amarr_dict,"Sell Min"))
                print("The Highest Sell Standard Deviation is:", max_stats(amarr_dict,"Sell StdDev"))
                print("The Highest Sell Median is:", max_stats(amarr_dict,"Sell Median"))
                print("The Highest Sell Percentile is:", max_stats(amarr_dict,"Sell Percentile"))
                print("The Smallest Buy Volume is:", min_stats(amarr_dict,"Buy Vol"))
                print("The Smallest Buy Average is:", min_stats(amarr_dict,"Buy Avg"))
                print("The Smallest Buy Max is:", min_stats(amarr_dict,"Buy Max"))
                print("The Smallest Buy Min is:", min_stats(amarr_dict,"Buy Min"))
                print("The Smallest Buy Standard Deviation is:", min_stats(amarr_dict,"Buy StdDev"))
                print("The Smallest Buy Median is:", min_stats(amarr_dict,"Buy Median"))
                print("The Smallest Buy Percentile is:", min_stats(amarr_dict,"Buy Percentile"))
                print("The Smallest Sell Vol is:", min_stats(amarr_dict,"Sell Vol"))
                print("The Smallest Sell Average is:", min_stats(amarr_dict,"Sell Avg"))
                print("The Smallest Sell Max is:", min_stats(amarr_dict,"Sell Max"))
                print("The Smallest Sell Min is:", min_stats(amarr_dict,"Sell Min"))
                print("The Smallest Sell Standard Deviation is:", min_stats(amarr_dict,"Sell StdDev"))
                print("The Smallest Sell Median is:", min_stats(amarr_dict,"Sell Median"))
                print("The Smallest Sell Percentile is:", min_stats(amarr_dict,"Sell Percentile"))
                print("Press Enter for the Next Station")
                input()
                print("Dodixie:")
                print("The Highest Buy Volume is:", max_stats(dodixie_dict,"Buy Vol"))
                print("The Highest Buy Average is:", max_stats(dodixie_dict,"Buy Avg"))
                print("The Highest Buy Max is:", max_stats(dodixie_dict,"Buy Max"))
                print("The Highest Buy Min is:", max_stats(dodixie_dict,"Buy Min"))
                print("The Highest Buy Standard Deviation is:", max_stats(dodixie_dict,"Buy StdDev"))
                print("The Highest Buy Median is:", max_stats(dodixie_dict,"Buy Median"))
                print("The Highest Buy Percentile is:", max_stats(dodixie_dict,"Buy Percentile"))
                print("The Highest Sell Vol is:", max_stats(dodixie_dict,"Sell Vol"))
                print("The Highest Sell Average is:", max_stats(dodixie_dict,"Sell Avg"))
                print("The Highest Sell Max is:", max_stats(dodixie_dict,"Sell Max"))
                print("The Highest Sell Min is:", max_stats(dodixie_dict,"Sell Min"))
                print("The Highest Sell Standard Deviation is:", max_stats(dodixie_dict,"Sell StdDev"))
                print("The Highest Sell Median is:", max_stats(dodixie_dict,"Sell Median"))
                print("The Highest Sell Percentile is:", max_stats(dodixie_dict,"Sell Percentile"))
                print("The Smallest Buy Volume is:", min_stats(dodixie_dict,"Buy Vol"))
                print("The Smallest Buy Average is:", min_stats(dodixie_dict,"Buy Avg"))
                print("The Smallest Buy Max is:", min_stats(dodixie_dict,"Buy Max"))
                print("The Smallest Buy Min is:", min_stats(dodixie_dict,"Buy Min"))
                print("The Smallest Buy Standard Deviation is:", min_stats(dodixie_dict,"Buy StdDev"))
                print("The Smallest Buy Median is:", min_stats(dodixie_dict,"Buy Median"))
                print("The Smallest Buy Percentile is:", min_stats(dodixie_dict,"Buy Percentile"))
                print("The Smallest Sell Vol is:", min_stats(dodixie_dict,"Sell Vol"))
                print("The Smallest Sell Average is:", min_stats(dodixie_dict,"Sell Avg"))
                print("The Smallest Sell Max is:", min_stats(dodixie_dict,"Sell Max"))
                print("The Smallest Sell Min is:", min_stats(dodixie_dict,"Sell Min"))
                print("The Smallest Sell Standard Deviation is:", min_stats(dodixie_dict,"Sell StdDev"))
                print("The Smallest Sell Median is:", min_stats(dodixie_dict,"Sell Median"))
                print("The Smallest Sell Percentile is:", min_stats(dodixie_dict,"Sell Percentile"))
                print("Press Enter for the Next Station")
                input()
                print("Jita:")
                print("The Highest Buy Volume is:", max_stats(jita_dict,"Buy Vol"))
                print("The Highest Buy Average is:", max_stats(jita_dict,"Buy Avg"))
                print("The Highest Buy Max is:", max_stats(jita_dict,"Buy Max"))
                print("The Highest Buy Min is:", max_stats(jita_dict,"Buy Min"))
                print("The Highest Buy Standard Deviation is:", max_stats(jita_dict,"Buy StdDev"))
                print("The Highest Buy Median is:", max_stats(jita_dict,"Buy Median"))
                print("The Highest Buy Percentile is:", max_stats(jita_dict,"Buy Percentile"))
                print("The Highest Sell Vol is:", max_stats(jita_dict,"Sell Vol"))
                print("The Highest Sell Average is:", max_stats(jita_dict,"Sell Avg"))
                print("The Highest Sell Max is:", max_stats(jita_dict,"Sell Max"))
                print("The Highest Sell Min is:", max_stats(jita_dict,"Sell Min"))
                print("The Highest Sell Standard Deviation is:", max_stats(jita_dict,"Sell StdDev"))
                print("The Highest Sell Median is:", max_stats(jita_dict,"Sell Median"))
                print("The Highest Sell Percentile is:", max_stats(jita_dict,"Sell Percentile"))
                print("The Smallest Buy Volume is:", min_stats(jita_dict,"Buy Vol"))
                print("The Smallest Buy Average is:", min_stats(jita_dict,"Buy Avg"))
                print("The Smallest Buy Max is:", min_stats(jita_dict,"Buy Max"))
                print("The Smallest Buy Min is:", min_stats(jita_dict,"Buy Min"))
                print("The Smallest Buy Standard Deviation is:", min_stats(jita_dict,"Buy StdDev"))
                print("The Smallest Buy Median is:", min_stats(jita_dict,"Buy Median"))
                print("The Smallest Buy Percentile is:", min_stats(jita_dict,"Buy Percentile"))
                print("The Smallest Sell Vol is:", min_stats(jita_dict,"Sell Vol"))
                print("The Smallest Sell Average is:", min_stats(jita_dict,"Sell Avg"))
                print("The Smallest Sell Max is:", min_stats(jita_dict,"Sell Max"))
                print("The Smallest Sell Min is:", min_stats(jita_dict,"Sell Min"))
                print("The Smallest Sell Standard Deviation is:", min_stats(jita_dict,"Sell StdDev"))
                print("The Smallest Sell Median is:", min_stats(jita_dict,"Sell Median"))
                print("The Smallest Sell Percentile is:", min_stats(jita_dict,"Sell Percentile"))
                print("Press Enter for the Next Station")
                input()
                print("Rens:")
                print("The Highest Buy Volume is:", max_stats(rens_dict,"Buy Vol"))
                print("The Highest Buy Average is:", max_stats(rens_dict,"Buy Avg"))
                print("The Highest Buy Max is:", max_stats(rens_dict,"Buy Max"))
                print("The Highest Buy Min is:", max_stats(rens_dict,"Buy Min"))
                print("The Highest Buy Standard Deviation is:", max_stats(rens_dict,"Buy StdDev"))
                print("The Highest Buy Median is:", max_stats(rens_dict,"Buy Median"))
                print("The Highest Buy Percentile is:", max_stats(rens_dict,"Buy Percentile"))
                print("The Highest Sell Vol is:", max_stats(rens_dict,"Sell Vol"))
                print("The Highest Sell Average is:", max_stats(rens_dict,"Sell Avg"))
                print("The Highest Sell Max is:", max_stats(rens_dict,"Sell Max"))
                print("The Highest Sell Min is:", max_stats(rens_dict,"Sell Min"))
                print("The Highest Sell Standard Deviation is:", max_stats(rens_dict,"Sell StdDev"))
                print("The Highest Sell Median is:", max_stats(rens_dict,"Sell Median"))
                print("The Highest Sell Percentile is:", max_stats(rens_dict,"Sell Percentile"))
                print("The Smallest Buy Volume is:", min_stats(rens_dict,"Buy Vol"))
                print("The Smallest Buy Average is:", min_stats(rens_dict,"Buy Avg"))
                print("The Smallest Buy Max is:", min_stats(rens_dict,"Buy Max"))
                print("The Smallest Buy Min is:", min_stats(rens_dict,"Buy Min"))
                print("The Smallest Buy Standard Deviation is:", min_stats(rens_dict,"Buy StdDev"))
                print("The Smallest Buy Median is:", min_stats(rens_dict,"Buy Median"))
                print("The Smallest Buy Percentile is:", min_stats(rens_dict,"Buy Percentile"))
                print("The Smallest Sell Vol is:", min_stats(rens_dict,"Sell Vol"))
                print("The Smallest Sell Average is:", min_stats(rens_dict,"Sell Avg"))
                print("The Smallest Sell Max is:", min_stats(rens_dict,"Sell Max"))
                print("The Smallest Sell Min is:", min_stats(rens_dict,"Sell Min"))
                print("The Smallest Sell Standard Deviation is:", min_stats(rens_dict,"Sell StdDev"))
                print("The Smallest Sell Median is:", min_stats(rens_dict,"Sell Median"))
                print("The Smallest Sell Percentile is:", min_stats(rens_dict,"Sell Percentile"))
                print("Press Enter to for the Next Station")
                input()
                print("User File:")
                print("The Highest Buy Volume is:", max_stats(my_dict,"Buy Vol"))
                print("The Highest Buy Average is:", max_stats(my_dict,"Buy Avg"))
                print("The Highest Buy Max is:", max_stats(my_dict,"Buy Max"))
                print("The Highest Buy Min is:", max_stats(my_dict,"Buy Min"))
                print("The Highest Buy Standard Deviation is:", max_stats(my_dict,"Buy StdDev"))
                print("The Highest Buy Median is:", max_stats(my_dict,"Buy Median"))
                print("The Highest Buy Percentile is:", max_stats(my_dict,"Buy Percentile"))
                print("The Highest Sell Vol is:", max_stats(my_dict,"Sell Vol"))
                print("The Highest Sell Average is:", max_stats(my_dict,"Sell Avg"))
                print("The Highest Sell Max is:", max_stats(my_dict,"Sell Max"))
                print("The Highest Sell Min is:", max_stats(my_dict,"Sell Min"))
                print("The Highest Sell Standard Deviation is:", max_stats(my_dict,"Sell StdDev"))
                print("The Highest Sell Median is:", max_stats(my_dict,"Sell Median"))
                print("The Highest Sell Percentile is:", max_stats(my_dict,"Sell Percentile"))
                print("The Smallest Buy Volume is:", min_stats(my_dict,"Buy Vol"))
                print("The Smallest Buy Average is:", min_stats(my_dict,"Buy Avg"))
                print("The Smallest Buy Max is:", min_stats(my_dict,"Buy Max"))
                print("The Smallest Buy Min is:", min_stats(my_dict,"Buy Min"))
                print("The Smallest Buy Standard Deviation is:", min_stats(my_dict,"Buy StdDev"))
                print("The Smallest Buy Median is:", min_stats(my_dict,"Buy Median"))
                print("The Smallest Buy Percentile is:", min_stats(my_dict,"Buy Percentile"))
                print("The Smallest Sell Vol is:", min_stats(my_dict,"Sell Vol"))
                print("The Smallest Sell Average is:", min_stats(my_dict,"Sell Avg"))
                print("The Smallest Sell Max is:", min_stats(my_dict,"Sell Max"))
                print("The Smallest Sell Min is:", min_stats(my_dict,"Sell Min"))
                print("The Smallest Sell Standard Deviation is:", min_stats(my_dict,"Sell StdDev"))
                print("The Smallest Sell Median is:", min_stats(my_dict,"Sell Median"))
                print("The Smallest Sell Percentile is:", min_stats(my_dict,"Sell Percentile"))
                print("Press Enter to Go Back to the Option 1 Menu")
                input()
            if answer == "2":
                print("Amarr: ")
                gen_stats(amarr_dict,"Buy Avg")
                print("This histogram is based on Buy Average.")
                print()
                gen_stats(amarr_dict,"Sell Avg")
                print("This histogram is based on Sell Average.")
                print()
                print("Press Enter for the Next Station")
                input()
                print("Dodixie: ")
                gen_stats(dodixie_dict,"Buy Avg")
                print("This histogram is based on Buy Average.")
                print()
                gen_stats(dodixie_dict,"Sell Avg")
                print("This histogram is based on Sell Average.")
                print()
                print("Press Enter for the Next Station")
                input()
                print("Jita: ")
                gen_stats(jita_dict,"Buy Avg")
                print("This histogram is based on Buy Average.")
                print()
                gen_stats(jita_dict,"Sell Avg")
                print("This histogram is based on Sell Average.")
                print()
                print("Press Enter for the Next Station")
                input()
                print("Rens: ")
                gen_stats(rens_dict,"Buy Avg")
                print("This histogram is based on Buy Average.")
                print()
                gen_stats(rens_dict,"Sell Avg")
                print("This histogram is based on Sell Average.")
                print()
                print("Press Enter for the Next Station")
                input()
                print("User File: ")
                gen_stats(my_dict,"Buy Avg")
                print("This histogram is based on Buy Average.")
                print()
                gen_stats(my_dict,"Sell Avg")
                print("This histogram is based on Sell Average.")
                print()
                print("Press Enter to Go Back to the Option 1 Menu")
                input()
            if answer == "3":
                status = False
            if answer not in list:
                print("Error: Invalid Input.")
                print()
                continue
       
    
    # Define function for all option 2 functionalities      
    def option2_2():
        list = ["1","2","3","4","5","6"]
        print("You have chosen to see statistics for specific trade stations")
        print()
        status = True
        while status:
            print (trade_stations_2)
            print()
            station = input("Choose which station you would like to use: ")
            print()
            if station == "1":
                going = True
                print("You have chosen Amarr.")
                print()
                while going:
                    print(station_options)
                    print()
                    choice = input("Choose one of the options above: ")
                    print()
                    if choice == "1":
                        all_stats(amarr_dict)
                    if choice == "2":
                        spec_stats(amarr_dict)
                    if choice == "3":
                        buy_stats(amarr_dict)
                    if choice == "4":
                        sell_stats(amarr_dict)
                    if choice == "5":
                        going = False
                    if choice not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
            if station == "2":
                going = True
                print("You have chosen Dodixie.")
                print()
                while going:
                    print(station_options)
                    print()
                    choice = input("Choose one of the options above: ")
                    print()
                    if choice == "1":
                        all_stats(dodixie_dict)
                    if choice == "2":
                        spec_stats(dodixie_dict)
                    if choice == "3":
                        buy_stats(dodixie_dict)
                    if choice == "4":
                        sell_stats(dodixie_dict)
                    if choice == "5":
                        going = False
                    if choice not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
            if station == "3":
                going = True
                print("You have chosen Jita.")
                print()
                while going:
                    print(station_options)
                    print()
                    choice = input("Choose one of the options above: ")
                    print()
                    if choice == "1":
                        all_stats(jita_dict)
                    if choice == "2":
                        spec_stats(jita_dict)
                    if choice == "3":
                        buy_stats(jita_dict)
                    if choice == "4":
                        sell_stats(jita_dict)
                    if choice == "5":
                        going = False
                    if choice not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
            if station == "4":
                going = True
                print("You have chosen Rens.")
                print()
                while going:
                    print(station_options)
                    print()
                    choice = input("Choose one of the options above: ")
                    print()
                    if choice == "1":
                        all_stats(rens_dict)
                    if choice == "2":
                        spec_stats(rens_dict)
                    if choice == "3":
                        buy_stats(rens_dict)
                    if choice == "4":
                        sell_stats(rens_dict)
                    if choice == "5":
                        going = False
                    if choice not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
            if station == "5":
                going = True
                print("You have chosen your own data file.")
                print()
                while going:
                    print(station_options)
                    print()
                    choice = input("Choose one of the options above: ")
                    print()
                    if choice == "1":
                        all_stats(my_dict)
                    if choice == "2":
                        spec_stats(my_dict)
                    if choice == "3":
                        buy_stats(my_dict)
                    if choice == "4":
                        sell_stats(my_dict)
                    if choice == "5":
                        going = False
                    if choice not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
            if station == "6":
                status = False
            if station not in list:
                print("Error: Invalid Input.")
                print()
                continue
    
    
    # Define function for all option 3 functionalities
    def option3_2():
        list = ["1","2"]
        status = True
        while status:
            answer = input("Please input an item name: ")
            answer = answer.lower()
            print()
            try:
                amarr_dict[answer]
                print("Amarr:")
                print_list(amarr_dict,answer)
                print()
                print("Jita:")
                print_list(jita_dict,answer)
                print("Dodixie:")
                print_list(dodixie_dict,answer)
                print()
                print("Rens:")
                print_list(rens_dict,answer)
                print()
                print("User File:")
                print_list(my_dict,answer)
                print()
                going = True
                while going:
                    answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
                    print()
                    if answer == "1":
                        status = True
                        going = False
                    elif answer == "2":
                        status = False
                        going = False
                    if answer not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
            except:
                print("Error: Item name not found. Please try again.")
    
    
    # Define function for all option 4 functionalities
    def option4_2():
        list = ["1","2","3"]
        status = True
        while status:
            print(spec_stats_options)
            print()
            station = input("Choose an option above: ")
            print()
            if station == "1":
                print (trade_stations_2)
                print()
                station_name = input("Choose the station you want to see: ")
                print()
                if station_name == "1":
                    spec_stats(amarr_dict)
                if station_name == "2":
                    spec_stats(dodixie_dict)
                if station_name == "3":
                    spec_stats(jita_dict)
                if station_name == "4":
                    spec_stats(rens_dict)
                if station_name == "5":
                    spec_stats(my_dict)
            if station == "2":
                all_spec_stats()
            if station == "3":
                status = False
            if station not in list:
                print("Error: Invalid Input.")
                print()
                continue
    filename = input("Please input the name of your file: ")
    print()
    global my_dict
    my_dict = build_dict(filename)
    going = True
    while going:
        print(options)
        print()
        choice = input("Choose one of the options above: ")
        print()
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
            going = False
        else:
            print("Error: Invalid input.")
            print()
            continue