import datetime
import json
from collections import defaultdict
from tabulate import tabulate
from matplotlib import pyplot as plt


file = open("leaderboard.json", encoding="utf8").read()

jsn = json.loads(file)
users = defaultdict(list)
members = jsn["members"]
for member_id in members:
    user = []
    member = members[member_id]
    name = member["name"]
    score = member["local_score"]
    completion = member["completion_day_level"]

    for day_index in completion:
        day = completion[day_index]
        star_1 = day["1"]
        time_1 = (datetime.datetime.fromtimestamp(star_1["get_star_ts"]) -
                  datetime.datetime(2023, 12, int(day_index), 6, 0))
        try:
            star_2 = day["2"]
            time_2 = (datetime.datetime.fromtimestamp(star_2["get_star_ts"]) -
                      datetime.datetime(2023, 12, int(day_index), 6, 0))
        except:
            time_2 = datetime.datetime(1000, 12, int(day_index), 6, 0) - datetime.datetime(2024, 1, 30, 0)
        user_stats = (day_index, time_1, time_2)
        # print("User:", name, "| Day:", day_index, "| Time for Star 1:", time_1, "| Time for Star 2:", time_2)
        user.append(user_stats)
    users[name] = [s for s in user]

users_sorted_by_day = defaultdict(list)
users_sorted_by_second_star = {}
users_sorted_by_first_star = {}

# Sorting users by day
for user, stats in users.items():
    users_sorted_by_day[user] = sorted(stats, key=lambda x: x[0])

# Sorting users by time taken for the second star
#users_sorted_by_second_star = sorted(users.items(), key=lambda x: (x[1][-1][2] - datetime.datetime(2023, 12, int(x[1][-1][0]), 6, 0)).total_seconds() if x[1] and x[1][-1][2] != datetime.datetime(1000, 12, int(x[1][-1][0]), 6, 0) - datetime.datetime(2024, 1, 30, 0) else float('inf'))

# Sorting users by time taken for the first star
#users_sorted_by_first_star = sorted(users.items(), key=lambda x: x[1][-1][1])

# Displaying the leaderboard
headers = ["User", "Day", "Time for Star 1", "Time for Star 2"]
for user, stats in users_sorted_by_day.items():
    print(f"\nLeaderboard for {user}:")
    print(tabulate(stats, headers=headers))

# Plotting a graph for the top users by time taken for the second star
top_users = 5  # You can adjust this number based on how many top users you want to display
plt.figure(figsize=(10, 6))
plt.title(f"Top {top_users} Users by Time for Second Star")
plt.xlabel("User")
plt.ylabel("Time (hours)")
for user, stats in users_sorted_by_second_star[:top_users]:
    day_index, time_1, time_2 = stats[-1]
    plt.bar(user, time_2.total_seconds() / 3600)

plt.show()
