speed = input("welcome to Download Calculator, what are your download speeds? (megabytes per second) ")
format = input("do you want to calculate megabytes or gigabytes? ")

#finds file format and calculates
if format == "gigabytes":
    size = input("what is the size of the file? (gigabytes) ")
    calculate = float(size)*1000/float(speed)
    time = int(calculate/60)
    hours = int(time/60)
    print("it will take roughly",time,"minutes, or", hours, " hours for your download to finish")

elif format == "megabytes":
    size = input("what is the size of the file? (megabytes) ")
    calculate = float(size)/float(speed)
    time = int(calculate/60)
    hours = int(time/60)
    print("it will take roughly",time,"minutes, or", hours, "hours for your download to finish")

#if incorrect format is entered
else: print("invalid format run program again")
