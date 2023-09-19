print('List of months: January, February, March, April, May, June, July, August, September, October, November, December')
name = input("Input the name of Month: ")
if(name == 'February'):
    print("No. of days: 28/29 days")
    
elif(name == "April" or name == "June" or name =="September" or name =="November"):
    print("No. of days: 30 days")
else:
     print("No. of days: 31 days")