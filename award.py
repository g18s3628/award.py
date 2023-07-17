#Request user to input the time for swimming, cycling and running in minutes
time_swimming = int(input("Duration for swimming (in minutes):"))
time_cycling = int(input("Duration for cycling (in minutes):"))
time_running = int(input("Duration for running (in minutes):"))

#Summation of all the times and name it total time
total_time = time_swimming + time_cycling + time_running

#If total time is less than or equal to 100 then print Provincial Colours
if total_time <= 100:
    print("Award: Within the qualifying time - Provincial Colours")
#If total time is ranges from 101 to 105 then print Provincial Half Colours
elif total_time <= 105: 
    print("Award: Within 5 minutes of the qualifying time - Provincial Half Colours")
#If total time is ranges from 106 to 110 then print Provincial Scroll
elif total_time <= 110:
    print("Award: Within 10 minutes  of the qualifying time - Provincial Scroll")
#If total time is ranges from 111 upwards then print No award
else:
    print("Award: More than 10 minutes off from the qualifying time - No award")
