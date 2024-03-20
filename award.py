#ask the user for the swimming, cycling and running times using the input functions
swim_time = int(input("What was your swim time in minutes?"))
cycle_time = int(input("What was your cycle time in minutes?"))
run_time = int(input("What was your run time in minutes?"))
#now add each of the times together to get the total triathlon time
total_time = swim_time + cycle_time + run_time
#display the total time taken
print("You completed the triathlon in " +  str(total_time) + " minutes")
#identify if the user falls into the first bracket, finishing in 100mins or faster
if total_time <= 100:
    print("you have been awarded Provincial Colours for finishing in " + str(total_time) + " minutes!")
#then increase the bracket for the athletes who finished within 5 mins of the qualifying time
elif total_time <= 105:
    print("You have been awarded Provincial Half Colours for finishing in " + str(total_time) + " minutes!")
#increase the boundry by another 5 minutes for athletes who finished within 10 mins of qualifying
elif total_time <= 110:
    print("You have been awarded the Provincial Scroll for finishing in " + str(total_time) + " minutes!")
#finally, if the athlete did not finish within 10 mins of the qualifying time, they did not recieve an award
else:
    print("Sorry! No award. You did not complete the triathlon within ten minutes of the qualifying time, better luck next time.")