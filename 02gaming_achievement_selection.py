print("=== Gaming Achievement Checker ===")
    
# Input
player_score=-1
time_played_hours=-1
enemies_defeated=-1

# player_score = int(input("Enter your player score: "))
# time_played_hours = int(input("Enter hours played: "))
# enemies_defeated = int(input("Enter enemies defeated: "))

while player_score<0 or time_played_hours<0 or enemies_defeated<0:
    print("positive values only, Can't be less then 0")
    player_score = int(input("Enter your player score: "))
    time_played_hours = int(input("Enter hours played: "))
    enemies_defeated = int(input("Enter enemies defeated: "))

# Selection logic
if player_score>=15000 and time_played_hours>=100:
    achievement="Legend"
elif player_score >= 10000 and time_played_hours >= 50:
    achievement = "Master Player"
elif enemies_defeated >= 1000:
    achievement = "Combat Expert"
elif time_played_hours >= 20:
    achievement = "Dedicated Gamer"
elif player_score >= 5000:
    achievement = "Rising Star"
else:
    achievement = "Newcomer"

# Output
print(f"\nCongratulations! You've earned: {achievement}")

if achievement == "Master Player" or achievement == "Legend":
    print("You've unlocked the secret bonus level!")