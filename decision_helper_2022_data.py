import json

# load the player stats data from the file (replace filename with your own)
with open("ipl2022.json", "r") as f:
    data = json.load(f)

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
    "DBFreq": -0.5,
    "BdryFreq": 1.5,
    "BdryPercent": 1,
    "ScoringBalls": 1.5,
    "Ones": 1,
    "Twos": 1.5,
    "Fours": 2,
    "Sixes": 4,
    "Outs": -1,
    "NotOuts": 1,
    "FiftyPlusRuns": 2,
    "Centuries": 5,
    "BattingAverage": 1.5,
}

# calculate the total score for each player in the current match
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
        scores[player_name] = {"score": score, "skill_name": skill_name}

# print all players and their scores
print("All players:")
for player, data in scores.items():
    score = data["score"]
    skill_name = data["skill_name"]
    print(f"{player} ({skill_name}): {score:.2f}")
