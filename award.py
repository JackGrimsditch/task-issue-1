# Ask the user for the swimming, cycling, and running times using the input functions
try:
    swim_time = int(input("What was your swim time in minutes? "))
    cycle_time = int(input("What was your cycle time in minutes? "))
    run_time = int(input("What was your run time in minutes? "))
except ValueError:
    print("Please enter valid numeric values for swim, cycle, and run times.")

# Calculate the total triathlon time
total_time = swim_time + cycle_time + run_time

# Display the total time taken
print("You completed the triathlon in " + str(total_time) + " minutes.")

# Determine the award based on the total time
if total_time <= 100:
    print("Congratulations! You have been awarded Provincial Colours for finishing in " + str(total_time) + " minutes!")
elif total_time <= 105:
    print("Congratulations! You have been awarded Provincial Half Colours for finishing in " + str(total_time) + " minutes!")
elif total_time <= 110:
    print("Congratulations! You have been awarded the Provincial Scroll for finishing in " + str(total_time) + " minutes!")
else:
    print("Sorry! No award. You did not complete the triathlon within ten minutes of the qualifying time. Better luck next time.")
