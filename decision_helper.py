import csv
import json

def calculate_data(team1, team2, team1_vs_team2_file):
    # load the player data for the current match from the file (replace filename with your own)
    with open(team1_vs_team2_file, "r") as f:
        match_data = json.load(f)

    # create a dictionary of players in the current match
    match_players = {}
    for player in match_data["Data"]["Value"]["players"]:
        match_players[player["name"]] = player

    batters_scores = calculate_batters_data(team1, team2, match_players)
    bowlers_scores = calculate_bowlers_data(team1, team2, match_players)
    all_rounders_scores = calculate_allrounders_data(team1, team2, match_players)

    # # write the scores to a CSV file
    filename = f"{team1}vs{team2}Data.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Player Name", "Skill", "Score", "Selection Percentage"])
        for row in batters_scores:
            writer.writerow(row)
            print(f"{row[0]} ({row[1]}): Score = {row[2]:.2f}, Sel_Per = {row[3]:.2f}")
        
        for row in bowlers_scores:
            writer.writerow(row)
            print(f"{row[0]} ({row[1]}): Score = {row[2]:.2f}, Sel_Per = {row[3]:.2f}")
        
        for row in all_rounders_scores:
            writer.writerow(row)
            print(f"{row[0]} ({row[1]}): Score = {row[2]:.2f}, Sel_Per = {row[3]:.2f}")
            
    print(f"Output written to {filename}")

def calculate_batters_data(team1, team2, match_players):
      # load the player stats data from the file (replace filename with your own)
    with open("most_runs_2022.json", "r") as f:
        data2022 = json.load(f)

    # load the player stats data for 2023 from the file (replace filename with your own)
    with open("most_runs_2023.json", "r") as f:
        data2023 = json.load(f)
    
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

    # calculate the total score for each player across both seasons
    cumulative_scores = {}
    for player in data2022["toprunsscorers"] + data2023["toprunsscorers"]:
        player_name = player["StrikerName"]
        if player_name in match_players:
            if match_players[player_name]["skill_name"] == "BATTER" or match_players[player_name]["skill_name"] == "WICKET KEEPER":
                if player_name not in cumulative_scores:
                    cumulative_scores[player_name] = {"2022": 0, "2023": 0}
                for season in ["2022", "2023"]:
                    weight = 0.75 if season == "2022" else 1
                    for stat, w in weights.items():
                        try:
                            value = float(player[stat])
                            cumulative_scores[player_name][season] += value * w * weight
                        except ValueError:
                            pass

    # calculate the final score for each player and write it to the CSV file
    scores = []
    for player_name, score_dict in cumulative_scores.items():
        skill_name = match_players[player_name]["skill_name"]
        sel_percent = match_players[player_name].get("sel_per", 0)
        final_score = sum(score_dict.values()) / 2
        scores.append([player_name, skill_name, final_score, sel_percent])

    # sort the scores in descending order of score
    scores.sort(key=lambda x: x[2], reverse=True)

    return scores
    # # write the scores to a CSV file
    # filename = f"{team1}vs{team2}Batters.csv"

    # with open(filename, "w", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["Player Name", "Skill", "Score", "Selection Percentage"])
    #     for row in scores:
    #         writer.writerow(row)
    #         print(f"{row[0]} ({row[1]}): Score = {row[2]:.2f}, Sel_Per = {row[3]:.2f}")
            
    # print(f"Batters Output written to {filename}")

def calculate_bowlers_data(team1, team2, match_players):
    # load the player stats data from the file (replace filename with your own)
    with open("most_wickets_2022.json", "r") as f:
        data2022 = json.load(f)

    # load the player stats data for 2023 from the file (replace filename with your own)
    with open("most_wickets_2023.json", "r") as f:
        data2023 = json.load(f)
    # define the weights for each statistic (tweak as necessary)
    weights = {
        "StrikeRate": 1.5,
        "TotalRunsConceded": -1,
        "DotBallsBowled": 2,
        "DotBallPercent": 1.5,
        "ScoringBallsBowled": -1,
        "BowlingAverage": 0.5,
        "BoundaryFrequency": -1.5,
        "BoundaryPercentage": -1,
        "EconomyRate": -1.5,
        "Ones": 1,
        "Twos": -0.5,
        "Fours": -2,
        "Sixes": -4,
        "Wides": -1,
        "NoBalls": -1,
        "Wickets": 8,
        "Maidens": 4,
        "MaidenWickets": 12,
        "FourWickets": 15,
        "FiveWickets": 18,
        "TenWickets": 50,
    }

    # calculate the total score for each player across both seasons
    cumulative_scores = {}
    for player in data2022["mostwickets"] + data2023["mostwickets"]:
        player_name = player["BowlerName"]
        if player_name in match_players:
            if match_players[player_name]["skill_name"] == "BOWLER":
                if player_name not in cumulative_scores:
                    cumulative_scores[player_name] = {"2022": 0, "2023": 0}
                for season in ["2022", "2023"]:
                    weight = 0.75 if season == "2022" else 1
                    for stat, w in weights.items():
                        try:
                            value = float(player[stat])
                            cumulative_scores[player_name][season] += value * w * weight
                        except ValueError:
                            pass

    # calculate the final score for each player and write it to the CSV file
    scores = []
    for player_name, score_dict in cumulative_scores.items():
        skill_name = match_players[player_name]["skill_name"]
        sel_percent = match_players[player_name].get("sel_per", 0)
        final_score = sum(score_dict.values()) / 2
        scores.append([player_name, skill_name, final_score, sel_percent])

    # sort the scores in descending order of score
    scores.sort(key=lambda x: x[2], reverse=True)
    return scores

    # # write the scores to a CSV file
    # filename = f"{team1}vs{team2}Bowler.csv"

    # with open(filename, "w", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["Player Name", "Skill", "Score", "Selection Percentage"])
    #     for row in scores:
    #         writer.writerow(row)
    #         print(f"{row[0]} ({row[1]}): Score = {row[2]:.2f}, Sel_Per = {row[3]:.2f}")
            
    # print(f"Bowler Output written to {filename}")

def calculate_allrounders_data(team1, team2, match_players):
    # load the player stats data from the file (replace filename with your own)
    all_rounder_2022_filename = f"{team1}vs{team2}2022.json"
    all_rounder_2023_filename = f"{team1}vs{team2}2023.json"
    with open(all_rounder_2022_filename, "r") as f:
        data2022 = json.load(f)

    # load the player stats data for 2023 from the file (replace filename with your own)
    with open(all_rounder_2023_filename, "r") as f:
        data2023 = json.load(f)
    # define the weights for each statistic (tweak as necessary)
    weights = {
        "BattingStrikeRate": 1.5,
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
        "BowlingStrikeRate": 1.5,
        "TotalRunsConceded": -1,
        "DotBallsBowled": 2,
        "DotBallPercent": 1.5,
        "ScoringBallsBowled": -1,
        "BowlingAverage": 0.5,
        "BoundaryFrequency": -1.5,
        "BoundaryPercentage": -1,
        "EconomyRate": -1.5,
        "Ones": 1,
        "Twos": -0.5,
        "Fours": -2,
        "Sixes": -4,
        "Wides": -1,
        "NoBalls": -1,
        "Wickets": 8,
        "Maidens": 4,
        "MaidenWickets": 12,
        "FourWickets": 15,
        "FiveWickets": 18,
        "TenWickets": 50,
    }

    # calculate the total score for each player across both seasons
    cumulative_scores = {}
    for player in data2022 + data2023:
        player_name = player["BowlerName"]
        if player_name in match_players:
            if match_players[player_name]["skill_name"] == "ALL ROUNDER":
                if player_name not in cumulative_scores:
                    cumulative_scores[player_name] = {"2022": 0, "2023": 0}
                for season in ["2022", "2023"]:
                    weight = 0.75 if season == "2022" else 1
                    for stat, w in weights.items():
                        try:
                            value = float(player[stat])
                            cumulative_scores[player_name][season] += value * w * weight
                        except ValueError:
                            pass

    # calculate the final score for each player and write it to the CSV file
    scores = []
    for player_name, score_dict in cumulative_scores.items():
        skill_name = match_players[player_name]["skill_name"]
        sel_percent = match_players[player_name].get("sel_per", 0)
        final_score = sum(score_dict.values()) / 2
        scores.append([player_name, skill_name, final_score, sel_percent])

    # sort the scores in descending order of score
    scores.sort(key=lambda x: x[2], reverse=True)
    return scores