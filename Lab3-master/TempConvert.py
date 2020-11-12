#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
    #Prompt the user for a Fahrenheit temperature
    Ftemp = int(input("Enter Temp in F: "))
    #Convert that temperature to celsius, rounding to 1 decimal percision
    Ctemp = (5/9)*(Ftemp-32)
    #Output converted temperature.
    print(round(Ctemp,1))
main()
