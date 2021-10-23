months ={
"1": "Jan",
"2": "Feb",
"3": "Mar",
"4": "Apr",
"5": "May",
"6": "Jun",
"7": "Jul",
"8": "Aug",
"9": "Sep",
"10": "Oct",
"11": "Nov",
"12": "Dec"
}

v = input("Enter month ")
if v in months:
    print("month %s is %s" %(v, months[v]))
else:
    print("Invalid value or Error")

