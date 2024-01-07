# Prompt the user for the number of times they have run around the racetrack
num_laps = int(input("Enter the number of times you have run around the racetrack: "))

lap_times = []  # List to store lap times

# Loop to prompt the user for lap times
for lap in range(num_laps):
    lap_time = float(input("Enter the lap time for lap {}: ".format(lap + 1)))
    lap_times.append(lap_time)

# Calculate the fastest lap, the slowest lap, and average lap time
fastest_lap = min(lap_times)
slowest_lap = max(lap_times)
average_lap = sum(lap_times) / num_laps

# Display the results
print("Fastest Lap Time: {:.2f}".format(fastest_lap))
print("Slowest Lap Time: {:.2f}".format(slowest_lap))
print("Average Lap Time: {:.2f}".format(average_lap))
