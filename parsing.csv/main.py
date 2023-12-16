file1 = open("Financials.csv", "r")
contents = file1.readlines()
file1.close()
for line in contents:
    info = line.split(",")
    if info[2] == 
                
