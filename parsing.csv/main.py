file1 = open("Financials.csv", "r")
contents = file1.readlines()
file1.close()
total = {}
lineNum = 0
for line in contents:
    lineNum += 1
    if lineNum == 1:
        continue
    pos = 0
    newline = ""
    for item in line:
        if(item == ","):
            before = line[pos-1]
            after = line[pos+1]
            date = line[pos-5]
            if(date == "/"):
                newline += item
                continue
            try: 
                before = int(before)
                after = int(after)
            except:
                newline += item
        else:
            newline += item
        pos += 1
    info = newline.split(",")
    fixed = info[7].replace("$", "")
    fixed = fixed.replace(" ", "")
    fixed = fixed.replace('"', "")
    if info[1] in total:
        years = total[info[1]]
        if info[15].strip() in years:
            years[info[15].strip()] += float(fixed)
        else:
            years[info[15].strip()] = float(fixed)
    else:
        total[info[1]] = {info[15].strip():float(fixed)}
for country in total:
    print(f"For {country}")
    for year in total[country]:
        print(f"In {year}")
        print(f"The total is ${total[country][year]}0")
