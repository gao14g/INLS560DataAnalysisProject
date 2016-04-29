from dictionary_builder import *


# Create options for choosing a certain station
trade_stations = """Option 1 - Amarr
Option 2 - Dodixie
Option 3 - Jita
Option 4 - Rens
Option 5 - Go Back to the Main Menu"""
  
# Create options for choosing to see certain types of statistics 
station_options = """Option 1 - Search for All Statistics for Specific Items
Option 2 - Search for Specific Statistics for Specific Items
Option 3 - Search for Buy Order Statistics for Specific Items
Option 4 - Search for Sell Order Statistics for Specific Items
Option 5 - Go Back to the Trade Stations Menu"""

# Create options for general statistics
general_options = """Option 1 - See Maximums and Minimums for Each Column 
Option 2 - See General Statistics for Each Data File
Option 3 - Go Back to the Main Menu"""

spec_stats_options = """Option 1 - See Items from a Specific Stations
Option 2 - See Items from All Stations
Option 3 - Go Back to the Main Menu"""


# Define function to determine ranges of items and print out histograms for those ranges
def gen_stats(trade_station,column):
    items = []
    for item in trade_station:
        items.append(trade_station[item][column])
        
    list1 = []
    count_1 = 0
    list2 = []
    count_2 = 0
    list3 = []
    count_3 = 0
    list4 = []
    count_4 = 0
    list5 = []
    count_5 = 0
    list6 = []
    count_6 = 0
    list7 = []
    count_7 = 0
    list8 = []
    count_8 = 0
    
    for number in items:
        number = number.replace(',','')
        number = float(number)
        if 0 < number <= 100:
            list1.append(number)
            count_1 += 1
        if 100 < number <= 1000:
            list2.append(number)
            count_2 += 1
        if 1000 < number <= 10000:
            list3.append(number)
            count_3 += 1
        if 10000 < number <= 100000:
            list4.append(number)
            count_4 += 1
        if 100001 < number <= 1000000:
            list5.append(number)
            count_5 += 1
        if 1000001 < number <= 10000000:
            list6.append(number)
            count_6 += 1
        if 10000001 < number <= 100000000:
            list7.append(number)
            count_7 += 1
        if number > 100000000:
            list8.append(number)
            count_8 += 1
            
    print ("Histogram of Number of Items Within the Range")
    print ("Range 0 - 100: " + "*"*(count_1//10))
    print ("Range 101 - 1,000: " + "*"*(count_2//10))
    print ("Range 1,001 - 10,000: " + "*"*(count_3//10))
    print ("Range 10,001 - 100,000: " + "*"*(count_4//10))
    print ("Range 100,001 - 1,000,000: " + "*"*(count_5//10))
    print ("Range 1,000,001 - 10,000,000: " + "*"*(count_6//10))
    print ("Range 10,000,001 - 100,000,000: " + "*"*(count_7//10))
    print ("Range 100,000,000+: " + "*"*(count_8//10)) 


# Define function to calculate the max number for each column
def max_stats(trade_station,column):
    items = []
    for item in trade_station:
        items.append(trade_station[item][column])
    
    largest = None
    for number in items:
        number = number.replace(',','')
        number = float(number)
        if largest is None or number > largest:
            largest = number
    return(largest)


# Define function to calculate the min number for each column
def min_stats(trade_station,column):
    items = []
    for item in trade_station:
        items.append(trade_station[item][column])
    
    smallest = None
    for number in items:
        number = number.replace(',','')
        number = float(number)
        if smallest is None or number < smallest:
            smallest = number
    return(smallest)


# Define function to show all statistics for a certain item
def all_stats(trade_station):
    list1 = ["1","2","help"]
    status = True
    while status:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        print()
        try:
            print_list(trade_station,answer)
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
                elif answer.lower() == "help":
                    help_message()
                if answer not in list1:
                    print("Error: Invalid Input.")
                    print()
                    continue
        except:
            print("Error: Item name not found. Please try again.")
            print()


# Define function to show all the buy order statistics for a certain item
def buy_stats(trade_station):
    list1 = ["1","2","help"]
    status = True
    while status:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        print()
        try:
            print_buy_stats(trade_station,answer)
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
                elif answer.lower() == "help":
                    help_message()
                if answer not in list1:
                    print("Error: Invalid Input.")
                    print()
                    continue
        except:
            print("Error: Item name not found. Please try again.")
            print()


# Define function to show all the sell order statistics for a certain item
def sell_stats(trade_station):
    list = ["1","2","help"]
    status = True
    while status:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        print()
        try:
            print_sell_stats(trade_station,answer)
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
                elif answer.lower() == "help":
                    help_message()
                if answer not in list:
                    print("Error: Invalid Input.")
                    print()
                    continue
        except:
            print("Error: Item name not found. Please try again.")
            print()


# Define function to print a list of all the columns for a certain item
def print_list(dictionary,answer):
    id = dictionary[answer]["ID"]
    buy_vol = dictionary[answer]["Buy Vol"]
    buy_avg = dictionary[answer]["Buy Avg"]
    buy_max = dictionary[answer]["Buy Max"]
    buy_min = dictionary[answer]["Buy Min"]
    buy_sdv = dictionary[answer]["Buy StdDev"]
    buy_med = dictionary[answer]["Buy Median"]
    buy_perc = dictionary[answer]["Buy Percentile"]
    sell_vol = dictionary[answer]["Sell Vol"]
    sell_avg = dictionary[answer]["Sell Avg"]
    sell_max = dictionary[answer]["Sell Max"]
    sell_min = dictionary[answer]["Sell Min"]
    sell_sdv = dictionary[answer]["Sell StdDev"]
    sell_med = dictionary[answer]["Sell Median"]
    sell_perc = dictionary[answer]["Sell Percentile"]
    print ("ID:", id)
    print ("Buy Volume:", buy_vol)
    print ("Buy Average:", buy_avg)
    print ("Buy Max:", buy_max)
    print ("Buy Min:", buy_min)
    print ("Buy Standard Deviation:", buy_sdv)
    print ("Buy Percentile:", buy_perc)
    print ("Sell Volume:", sell_vol)
    print ("Sell Average:", sell_avg)
    print ("Sell Max:", sell_max)
    print ("Sell Min:", sell_min)
    print ("Sell Standard Deviation:", sell_sdv)
    print ("Sell Percentile:", sell_perc)


# Define a function to print the buy order statistics for a certain item
def print_buy_stats(dictionary,answer):
    buy_vol = dictionary[answer]["Buy Vol"]
    buy_avg = dictionary[answer]["Buy Avg"]
    buy_max = dictionary[answer]["Buy Max"]
    buy_min = dictionary[answer]["Buy Min"]
    buy_sdv = dictionary[answer]["Buy StdDev"]
    buy_med = dictionary[answer]["Buy Median"]
    buy_perc = dictionary[answer]["Buy Percentile"]
    print ("Buy Volume:", buy_vol)
    print ("Buy Average:", buy_avg)
    print ("Buy Max:", buy_max)
    print ("Buy Min:", buy_min)
    print ("Buy Standard Deviation:", buy_sdv)
    print ("Buy Percentile:", buy_perc)


# Define a function to print the sell order statistics for a certain item
def print_sell_stats(dictionary,answer):
    sell_vol = dictionary[answer]["Sell Vol"]
    sell_avg = dictionary[answer]["Sell Avg"]
    sell_max = dictionary[answer]["Sell Max"]
    sell_min = dictionary[answer]["Sell Min"]
    sell_sdv = dictionary[answer]["Sell StdDev"]
    sell_med = dictionary[answer]["Sell Median"]
    sell_perc = dictionary[answer]["Sell Percentile"]
    print ("Sell Volume:", sell_vol)
    print ("Sell Average:", sell_avg)
    print ("Sell Max:", sell_max)
    print ("Sell Min:", sell_min)
    print ("Sell Standard Deviation:", sell_sdv)
    print ("Sell Percentile:", sell_perc)


# Define a function that allows the user to input the columns they want to see for a certain item for certain trade stations
def spec_stats(trade_station):
    list = ["1","2","help"]
    status = True
    while status:  
        item = input("Please input an item name: ")
        item = item.lower()
        print()
        try:
            trade_station[item]
            print("Please input the statistics you want to see separated by commas with no spaces before or after the column name.")
            print("Note: You must input the column names how it is found in the data. Example--Buy Vol,Buy Avg,Sell Vol,Sell Avg.")
            print("Type 'help' to see a list of column names.")
            answer = input()
            if answer.lower() == "help":
                help_message()
            else:
                try:
                    print()
                    answer_list = answer.split(",")
                    for stat in answer_list:
                        print(stat,":",trade_station[item][stat])
                except:
                    print("Error: Invalid Column Names.")
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
                    elif answer.lower() == "help":
                        help_message()
                    if answer not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
        except:
            print("Error: Item doesn't exist. Please try again.")
            print()


# Define a function that allows the user to input the columsn they want to see for a certain item for all trade stations
def all_spec_stats():
    list = ["1","2","help"]
    status = True
    while status:  
        item = input("Please input an item name: ")
        item = item.lower()
        print()
        try:
            amarr_dict[item]
            print("Please input the statistics you want to see separated by commas with no spaces before or after the column name.")
            print("Note: You must input the column names how it is found in the data. Example--Buy Vol,Buy Avg,Sell Vol,Sell Avg.")
            print("Type 'help' to see a list of column names.")
            answer = input()
            if answer.lower() == "help":
                help_message()
            else:
                try:
                    answer_list = answer.split(",")
                    print("Amarr:")
                    for stat in answer_list:
                        print(stat,":",amarr_dict[item][stat])
                    print()
                    print("Dodixie:")
                    for stat in answer_list:
                        print(stat,":",dodixie_dict[item][stat])
                    print()
                    print("Jita")
                    for stat in answer_list:
                        print(stat,":",jita_dict[item][stat])
                    print()
                    print("Rens:")
                    for stat in answer_list:
                        print(stat,":",rens_dict[item][stat])
                    print()
                except:
                    print("Error: Invalid Column Names")
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
                    elif answer.lower() == "help":
                        help_message()
                    if answer not in list:
                        print("Error: Invalid Input.")
                        print()
                        continue
        except:
            print("Error: Item doesn't exist. Please try again.")
            print()


# Define a function that prints out helpful tips and information for the user
def help_message():
    message = """Here are some extra tips and information:
    The data is broken down into these main columns:
    - ID
    - Buy Vol
    - Buy Avg
    - Buy Max
    - Buy Min
    - Buy StdDev
    - Buy Median
    - Buy Percentile
    - Sell Vol
    - Sell Avg
    - Sell Max
    - Sell Min
    - Sell StdDev
    - Sell Median
    - Sell Percentile
    The 'Buy' statistics refer to buy orders and the 'Sell' statistics refer to sell orders.
    Some examples of items in this list include:
    - Isogen, Griffin, Tristan, Kestrel, Utu, Vangel, Small Arms, Lucent Compound"""
    print (message)
    print("Press 'enter' to go back to the menu.")
    input()
