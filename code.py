with open("http_access_log.txt") as file_in:
    array = []
    for line in file_in:
        array.append(line)

comp = 0
dc = 0
wcomp = 0
wc = 0
mcomp = ""
mc = 0

for i in array:
    if i.find("[") != -1:
        dl = i.find("[")
        day = i[dl+1:dl+3]
        month = i[dl+4:dl+7]

        if comp == 0:
            comp = day
            mcomp = month
            dc += 1
        elif comp == day:
            dc += 1
        else:
            year = i[dl+8:dl+12]
            if mcomp != month:
                print("\nThere were " + str(mc) + " requests made over the span of " + mcomp + " " + year +".\n")
                mcomp = month
                mc = 0

            print("There were " + str(dc) + " requests made on " + month + " " + day + ", " + year + ".")
            wc += dc
            mc += dc
            comp = day 
            dc = 1
            wcomp += 1
            if (wcomp == 7):
                wcomp = 0
                print("\nThere were " + str(wc) + " requests made over the span of a week.\n")
                wc = 0

print("\nThere were " + str(mc) + " requests made over the span of " + mcomp + " " + year +".\n")