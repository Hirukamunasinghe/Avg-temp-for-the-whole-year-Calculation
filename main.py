#Qustion 2
import sys
#Initializing variables
total_daily_reading = 0
days_in_year = 2
daily_reading = 10
total_year_reading = 0
#Year
for day in range(1, days_in_year + 1):
    print(f"Day {day}")
    for daily_read in range(1, daily_reading + 1):
        single_daily_reading =input (f"Enter today's reading {daily_read}: ")
        #Validation
        try:
            val = float(single_daily_reading)
            total_daily_reading = total_daily_reading + val
            # If there is any value error this exception will catch and run the relevant code block
        except ValueError:
            print("[Error]- Invalid input!")
            #To exit the program after an occurrence of value error
            sys.exit()


    #Calculating the average daily temperature
    average_daily_temp = total_daily_reading / daily_reading
    print(f"The average daily temperature is {average_daily_temp}")
        #Calculating the total year reading
    total_year_reading += total_daily_reading
        #Calculating the average temperature for the whole year
avg_year_temp = total_year_reading / days_in_year
print(f"The average yearly temperature is {avg_year_temp}")
#End of code

