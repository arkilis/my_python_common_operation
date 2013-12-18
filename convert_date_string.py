# for some date string like Fri Apr  5 20:00:14 2013
# convert it to 2013-8-5


fp=open("temp.txt")
for line in fp.readlines():
    #print line # debug
    line= line.replace("  "," ")
    line= line.replace("\n","")
    ay_ele= line.split(" ")
    #print ay_ele,len(ay_ele)

    sz_new_date=ay_ele[4]
    if(ay_ele[1]=="Jan"):
        sz_new_date+="/01"
    elif(ay_ele[1]=="Feb"):
        sz_new_date+="/02"
    elif(ay_ele[1]=="Mar"):
        sz_new_date+="/03"
    elif(ay_ele[1]=="Apr"):
        sz_new_date+="/04"
    elif(ay_ele[1]=="May"):
        sz_new_date+="/05"
    elif(ay_ele[1]=="Jun"):
        sz_new_date+="/06"
    elif(ay_ele[1]=="Jul"):
        sz_new_date+="/07"
    elif(ay_ele[1]=="Aug"):
        sz_new_date+="/08"
    elif(ay_ele[1]=="Sep"):
        sz_new_date+="/09"
    elif(ay_ele[1]=="Oct"):
        sz_new_date+="/10"
    elif(ay_ele[1]=="Nov"):
        sz_new_date+="/11"
    else:
        sz_new_date+="/12"

    sz_new_date+="/"+ay_ele[2]+" "+ay_ele[3]

    print sz_new_date
