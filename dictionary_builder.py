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
    

# Define function to read in user files
def build_dict(filename):
    with open(filename) as file:
        file_lines = file.readlines()
    
    new_table = []
    for line in file_lines:
        new_table.append(line.split("\t"))
    
    for row in new_table:
        del row[17:len(new_table)+1]    
    global new_dict
    new_dict = {}
    for row in new_table[1:]:
        word = row[1]
        word = word.lower()
        if word not in new_dict:
            new_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
        else:
            new_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    return new_dict
