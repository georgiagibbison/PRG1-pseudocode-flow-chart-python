# Input: videos watched, average length
# Output: total time, equivalent in days

# Input
videos_watched=input("enter number of videos watched")
average_length=input("enter average video length (minutes)")

#Calculations
total_time=videos_watched*average_length
total_hours=total_time/60
in_days=total_hours/24

#Output
print(f"total time spent watching videos is {total_time}:.1f")
print(f"in days, that is {in_days}:.1f")