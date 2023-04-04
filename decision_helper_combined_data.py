import csv
import json

# load the player stats data from the file (replace filename with your own)
with open("ipl2022.json", "r") as f:
    data2022 = json.load(f)

# load the player stats data for 2023 from the file (replace filename with your own)
with open("ipl2023.json", "r") as f:
    data2023 = json.load(f)

# load the player data for the current match from the file (replace filename with your own)
with open("match.json", "r") as f:
    match_data = json.load(f)

# create a dictionary of players in the current match
match_players = {}
for player in match_data["Data"]["Value"]["players"]:
    match_players[player["name"]] = player

# define the weights for each statistic (tweak as necessary)
weights = {
    "StrikeRate": 1.5,
    "DBFreq": 1,
    "BdryFreq": 1,
    "BdryPercent": 1,
    "ScoringBalls": 1.5,
    "Ones": 0.5,
    "Twos": 1,
    "Fours": 1.5,
    "Sixes": 2,
    "Outs": -2,
    "NotOuts": 1,
    "FiftyPlusRuns": 2,
    "Centuries": 5,
    "BattingAverage": 1.5,
}

# calculate the total score and selection percentage for each player in the current match
scores = []
for player in data2022["toprunsscorers"] + data2023["toprunsscorers"]:
    player_name = player["StrikerName"]
    if player_name in match_players:
        score = 0
        for stat, weight in weights.items():
            try:
                value = float(player[stat])
                score += value * weight
            except ValueError:
                continue  # skip calculation for non-numeric values
        player_data = match_players[player_name]
        skill_name = player_data["skill_name"]
        sel_percent = player_data.get("sel_per", 0)
        scores.append([player_name, skill_name, score, sel_percent])

# sort the scores in descending order of score
scores.sort(key=lambda x: x[2], reverse=True)

# write the scores to a CSV file
team1_name = "DC"
team2_name = "GT"
filename = f"{team1_name}vs{team2_name}.csv"

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Player Name", "Skill", "Score", "Selection Percentage"])
    for row in scores:
        writer.writerow(row)
        print(f"{row[0]} ({row[1]}): Score = {row[2]:.2f}, Sel_Per = {row[3]:.2f}")
        
print(f"Output written to {filename}")
