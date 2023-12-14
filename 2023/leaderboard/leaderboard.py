import datetime
import json
from collections import defaultdict
from tabulate import tabulate
from matplotlib import pyplot as plt


file = open("leaderboard.json", encoding="utf8").read()

jsn = json.loads(file)
users = defaultdict()
members = jsn["members"]
ranking_per_day = defaultdict(list)
for member_id in members:
    user = []
    member = members[member_id]
    name = member["name"]
    score = member["local_score"]
    completion = member["completion_day_level"]
    star_2 = ()
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
        ranking_per_day[(day_index, 1, star_1["star_index"])] = (time_1, name)
        if star_2:
            ranking_per_day[(day_index, 2, star_2["star_index"])] = (time_2, name)
        # print("User:", name, "| Day:", day_index, "| Time for Star 1:", time_1, "| Time for Star 2:", time_2)
        user.append(user_stats)
    users[name] = [s for s in user]
users_sorted_by_day = defaultdict(list)
users_sorted_by_second_star = {}
users_sorted_by_first_star = {}

# Sorting users by day
for user, stats in users.items():
    users_sorted_by_day[user] = sorted(stats, key=lambda x: x[0])

interested_users = ["Cuubeyy", "Papierkorb2292", "raubtiermodus"]#, "Robocraft999", "Christian Schefe", "cmacht"]
for day, part, star in sorted(ranking_per_day):
    time, name = ranking_per_day[(day, part, star)]
    if name in interested_users:
        print(day, part, name, time)


