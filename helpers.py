#~/.bashrc

# Open Amarr.tsv file
with open("Amarr.tsv") as file:
    file_lines = file.readlines()

# Read through file and split based on tabs
amarr_table = []
for line in file_lines:
    amarr_table.append(line.split("\t"))


# Create a dictionary of dictionaries for each item with their statistics    
for row in amarr_table:
    del row[17:len(amarr_table)+1]    
amarr_dict = {}
for row in amarr_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in amarr_dict:
        amarr_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        amarr_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Open Jita.tsv file
with open("Jita.tsv") as file:
    file_lines = file.readlines()

# Read through file and split based on tabs
jita_table = []
for line in file_lines:
    jita_table.append(line.split("\t"))
 
# Create a dictionary of dictionaries for each item with their statistics  
for row in jita_table:
    del row[17:len(jita_table)+1]    
jita_dict = {}
for row in jita_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in jita_dict:
        jita_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        jita_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Open Dodixie.tsv file
with open("Dodixie.tsv") as file:
    file_lines = file.readlines()

# Read through the file and split based on tabs
dodixie_table = []
for line in file_lines:
    dodixie_table.append(line.split("\t"))
 
# Create a dictionary of dictionaries for each item with their statistics  
for row in dodixie_table:
    del row[17:len(dodixie_table)+1]    
dodixie_dict = {}
for row in dodixie_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in dodixie_dict:
        dodixie_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        dodixie_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Open Rens.tsv file
with open("Rens.tsv") as file:
    file_lines = file.readlines()

# Read through the file and split based on tabs
rens_table = []
for line in file_lines:
    rens_table.append(line.split("\t"))

# Create a dictionary of dictionaries for each item with their statistics  
for row in rens_table:
    del row[17:len(rens_table)+1]    
rens_dict = {}
for row in rens_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in rens_dict:
        rens_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        rens_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Create options for choosing a certain station
trade_stations = """Option 1 - Amarr
Option 2 - Dodixie
Option 3 - Jita
Option 4 - Rens """
  
# Create options for choosing to see certain types of statistics 
station_options = """Option 1 - Search for All Statistics for Specific Items
Option 2 - Search for Specific Statistics for Specific Items
Option 3 - Search for Buy Order Statistics for Specific Items
Option 4 - Search for Sell Order Statistics for Specific Items
Option 5 - Go Back to the Main Menu"""

general_options = """Option 1 -  See Comparative Statistics among All data Files
Option 2 -  See Maximums and Minimums for Each Column 
Option 3 -  See General Statistics for Each Data File"""

def option1():
    print (general_options)
    answer = input("Choose one of the options above: ")
    if answer == "2":
        print("Here are some general statistics about the data files")
        print("Amarr:")
        print("There are 1214 rows in this data file.")
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
        print("There are 1214 rows in this data file.")
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
        print("There are 1214 rows in this data file.")
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
        print("There are 1214 rows in this data file.")
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
        print("Press Enter to Go Back to the Main Menu")
        input()
    if answer == "3":
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
        print("Press Enter to Go Back to the Main Menu")
        input()
   
            
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
    print ("Range 0 - 100: " + "*"*(count_1))
    print ("Range 101 - 1,000: " + "*"*(count_2))
    print ("Range 1,001 - 10,000: " + "*"*(count_3))
    print ("Range 10,001 - 100,000: " + "*"*(count_4))
    print ("Range 100,001 - 1,000,000: " + "*"*(count_5))
    print ("Range 1,000,001 - 10,000,000: " + "*"*(count_6))
    print ("Range 10,000,001 - 100,000,000: " + "*"*(count_7))
    print ("Range 100,000,000+: " + "*"*(count_8)) 


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

# define function to show all statistics for a certain item
def all_stats(trade_station):
    going = True
    while going:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        try:
            print_list(trade_station,answer)
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                going = True
            elif answer == "2":
                going = False
        except:
            print("Error: Item name not found. Please try again.")

def buy_stats(trade_station):
    status = True
    while status:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        try:
            print_buy_stats(trade_station,answer)
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item name not found. Please try again.")

def sell_stats(trade_station):
    status = True
    while status:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        try:
            print_sell_stats(trade_station,answer)
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item name not found. Please try again.")
        
def option2():
    going = True
    print("You have chosen to see statistics for specific trade stations")
    print (trade_stations)
    station = input("Choose which station you would like to use: ")
    if station == "1":
        print("You have chosen Amarr.")
        while going:
            print(station_options)
            choice = input("Choose one of the options above: ")
            if choice == "1":
                all_stats(amarr_dict)
            if choice == "2":
                spec_stats(amarr_dict)
            if choice == "3":
                buy_stats(amarr_dict)
            if choice == "4":
                sell_stats(amarr_dict)
    if station == "2":
        print("You have chosen Dodixie.")
        print(station_options)
        choice = input("Choose one of the options above: ")
        if choice == "1":
            all_stats(dodixie_dict)
        if choice == "2":
            spec_stats(dodixie_dict)
        if choice == "3":
            buy_stats(dodixie_dict)
        if choice == "4":
            sell_stats(dodixie_dict)
    if station == "3":
        print("You have chosen Jita")
        print(station_options)
        choice = input("Choose one of the options above: ")
        if choice == "1":
            all_stats(jita_dict)
        if choice == "2":
            spec_stats(jita_dict)
        if choice == "3":
            buy_stats(jita_dict)
        if choice == "4":
            sell_stats(jita_dict)
    if station == "4":
        print("You have chosen Rens.")
        print(station_options)
        choice = input("Choose one of the options above: ")
        if choice == "1":
            all_stats(rens_dict)
        if choice == "2":
            spec_stats(rens_dict)
        if choice == "3":
            buy_stats(rens_dict)
        if choice == "4":
            sell_stats(rens_dict)
    if station == "5":
        going = False


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
    
def option3():
    status = True
    while status:
        answer = input("Please input an item name: ")
        answer = answer.lower()
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
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item name not found. Please try again.")

def spec_stats(trade_station):
    status = True
    while status:  
        item = input("Please input an item name: ")
        item = item.lower()
        try:
            trade_station[item]
            answer = input("Please input the statistics you want to see separated by commas with no spaces: ")
            answer_list = answer.split(",")
            for stat in answer_list:
                print(stat,":",trade_station[item][stat])
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item doesn't exist. Please try again.")

def all_spec_stats():
    status = True
    while status:  
        item = input("Please input an item name: ")
        item = item.lower()
        try:
            amarr_dict[item]
            answer = input("Please input the statistics you want to see separated by commas with no spaces: ")
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
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item doesn't exist. Please try again.")
    
def option4():
    status = True
    while status:
        station = input("Type '1' if you want to see items from a specific station, type '2' if you want to see items from all stations, or type '3' to go back to the main menu: ")
        if station == "1":
            print (trade_stations)
            station_name = input("Choose the station you want to see: ")
            if station_name == "1":
                spec_stats(amarr_dict)
            if station_name == "2":
                spec_stats(dodixie_dict)
            if station_name == "3":
                spec_stats(jita_dict)
            if station_name == "4":
                spec_stats(rens_dict)
        if station == "2":
            all_spec_stats()
        if station == "3":
            status = False

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
    The 'Buy' statstics refer to buy orders and the 'Sell' statstics refer to sell orders.
    Some examples of items in this list include:
    - Isogen, Griffin, Tristan, Kestrel, Utu, Vangel, Small Arms, Lucent Compound"""
    print (message)
    print("Press 'enter' to go back to the menu.")
    input()
    