import json

# load the player stats data for both years from the files (replace filenames with your own)
with open("ipl2022.json", "r") as f:
    ipl2022_data = json.load(f)

with open("ipl2023.json", "r") as f:
    ipl2023_data = json.load(f)

# combine the player stats data from both years
data = {"toprunsscorers": ipl2022_data["toprunsscorers"] + ipl2023_data["toprunsscorers"]}

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
scores = {}
for player in data["toprunsscorers"]:
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
        sel_per = player_data["sel_per"]
        scores[player_name] = {"score": score, "skill_name": skill_name, "sel_per": sel_per}

# print all players and their scores sorted by score in descending order, along with their selection percentage
print("All players:")
for player, data in sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True):
    score = data["score"]
    skill_name = data["skill_name"]
    sel_per = data["sel_per"]
    print(f"{player} ({skill_name}): {score:.2f}, Selection percentage: {sel_per}")