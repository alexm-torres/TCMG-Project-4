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

from collections import Counter

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

tr = 0
ncc = 0
rec = 0

arr2 = []

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
            tr += dc
            comp = day 
            dc = 1
            wcomp += 1
            if (wcomp == 7):
                wcomp = 0
                print("\nThere were " + str(wc) + " requests made over the span of a week.\n")
                wc = 0

    if i.find("0"") != -1:
        scl = i.find("0"") + 3

        sc = i[scl:scl+1]

        if(sc == "3"):
            rec += 1

        if(sc == "4"):
            ncc += 1

    if i.find("GET ") != -1:
        fl = i.find("GET ") + 4
        fel = i.find(" HTTP")
        file = i[fl:fel]
        arr2.append(file)

print("\nThere were " + str(mc) + " requests made over the span of " + mcomp + " " + year +".\n") 
nccper = (ncc/tr) * 100.0
recper = (rec/tr) * 100.0

print(str(nccper) + "% of the requests were not successful.")
print(str(recper) + "% of the requests were redirected elsewhere.\n")

c = Counter(arr2)
mc = c.most_common()[0]
lc = c.most_common()[-1]
print("The most-requested file was " + str(mc[0]) + ".")
print("The least-requested file was " + str(lc[0]) + ".")