with open("http_access_log.txt") as file_in:
    array = []
    for line in file_in:
        array.append(line)

comp = 0
dc = 0


for i in array:
    if i.find("[") != -1:
        dl = i.find("[")
        day = i[dl+1:dl+3]

        if comp == 0:
            comp = day
            dc += 1
        elif comp == day:
            dc += 1
        else:
            month = i[dl+4:dl+7]
            year = i[dl+8:dl+12]
            print("There were " + str(dc) + " requests made on " + month + " " + day + ", " + year + ".")
            comp = day 
            dc = 1