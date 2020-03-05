import datetime

def ageCalculator():
    day = int(input("Enter Day of Birth: \n"))
    month = int(input("Enter Month of Birth \n"))
    year = int(input("Enter Year of Birth: \n"))
    current_year = datetime.datetime.now().year;
    age = current_year-year
    print("Date of birth is dd/mm/yyyy: ",day,"/",month,"/",year)
    print("You are ", age,"years old")
    
ageCalculator()
