import json

def merge_data (year, team1, team2, teams_filename):
    
    # Load data from JSON files
    wickets_file_name = f"most_wickets_{year}.json"
    runs_file_name = f"most_runs_{year}.json"

    with open(wickets_file_name, 'r') as f:
        wickets_data = json.load(f)

    with open(runs_file_name, 'r') as f:
        runs_data = json.load(f)

    with open(teams_filename, 'r') as f:
        teams_data = json.load(f)

    # Extract all-rounders from teams.json
    all_rounders = [player for player in teams_data['Data']['Value']['players'] if player['skill_name'] == 'ALL ROUNDER']

    # Combine data for each all-rounder
    all_rounders_data = []
    for all_rounder in all_rounders:
        name = all_rounder['name']
        player_data = {}
        for bowler in wickets_data['mostwickets']:
            if bowler['BowlerName'] == name:
                for batsman in runs_data['toprunsscorers']:
                    if batsman['StrikerName'] == name:
                        # Create a dictionary for the player's data
                        player_data['StrikerName'] = batsman['StrikerName']
                        player_data['PlayerId'] = batsman['PlayerId']
                        player_data['Matches'] = batsman['Matches']
                        player_data['PlayerDOB'] = batsman['PlayerDOB']
                        player_data['RightHandedBat'] = batsman['RightHandedBat']
                        player_data['Nationality'] = batsman['Nationality']
                        player_data['TCompetitionID'] = batsman['TCompetitionID']
                        player_data['TStrikerID'] = batsman['TStrikerID']
                        player_data['TTeamID'] = batsman['TTeamID']
                        player_data['TeamCode'] = batsman['TeamCode']
                        player_data['TeamName'] = batsman['TeamName']
                        player_data['CompetitionID'] = batsman['CompetitionID']
                        player_data['TeamID'] = batsman['TeamID']
                        player_data['StrikerID'] = batsman['StrikerID']
                        player_data['Innings'] = batsman['Innings']
                        player_data['Extras'] = batsman['Extras']
                        player_data['TotalRuns'] = batsman['TotalRuns']
                        player_data['Balls'] = batsman['Balls']
                        player_data['Dotballs'] = batsman['Dotballs']
                        player_data['BattingStrikeRate'] = batsman['StrikeRate']
                        player_data['DBPercent'] = batsman['DBPercent']
                        player_data['DBFreq'] = batsman['DBFreq']
                        player_data['BdryFreq'] = batsman['BdryFreq']
                        player_data['BdryPercent'] = batsman['BdryPercent']
                        player_data['RPSS'] = batsman['RPSS']
                        player_data['ScoringBalls'] = batsman['ScoringBalls']
                        player_data['Ones'] = batsman['Ones']
                        player_data['Twos'] = batsman['Twos']
                        player_data['Threes'] = batsman['Threes']
                        player_data['Fours'] = batsman['Fours']
                        player_data['Sixes'] = batsman['Sixes']
                        player_data['Outs'] = batsman['Outs']
                        player_data['NotOuts'] = batsman['NotOuts']
                        player_data['BattingAveragesss'] = batsman['BattingAveragesss']
                        player_data['FiftyPlusRuns'] = batsman['FiftyPlusRuns']
                        player_data['Centuries'] = batsman['Centuries']
                        player_data['DoubleCenturies'] = batsman['DoubleCenturies']
                        player_data['HighestScore'] = batsman['HighestScore']
                        player_data['BattingAverage'] = batsman['BattingAverage']
                        player_data['Catches'] = batsman['Catches']
                        player_data['Stumpings'] = batsman['Stumpings']
                        player_data['BattingClientPlayerID'] = batsman['ClientPlayerID']
                        player_data["BowlerName"] = bowler["BowlerName"]
                        player_data["RightHandedBat"] = bowler["RightHandedBat"]
                        player_data["Nationality"] = bowler["Nationality"]
                        player_data["TeamCode"] = bowler["TeamCode"]
                        player_data["TeamName"] = bowler["TeamName"]
                        player_data["Matches"] = bowler["Matches"]
                        player_data["CompetitionID"] = bowler["CompetitionID"]
                        player_data["Innings"] = bowler["Innings"]
                        player_data["TeamID"] = bowler["TeamID"]
                        player_data["BowlerID"] = bowler["BowlerID"]
                        player_data["LegalBallsBowled"] = bowler["LegalBallsBowled"]
                        player_data["TotalRunsConceded"] = bowler["TotalRunsConceded"]
                        player_data["DotBallsBowled"] = bowler["DotBallsBowled"]
                        player_data["DotBallPercent"] = bowler["DotBallPercent"]
                        player_data["ScoringBallsBowled"] = bowler["ScoringBallsBowled"]
                        player_data["BowlingAverage"] = bowler["BowlingAverage"]
                        player_data["BowlingStrikeRate"] = bowler["StrikeRate"]
                        player_data["BowlingSR"] = bowler["BowlingSR"]
                        player_data["BoundaryPercentage"] = bowler["BoundaryPercentage"]
                        player_data["BoundaryFrequency"] = bowler["BoundaryFrequency"]
                        player_data["EconomyRate"] = bowler["EconomyRate"]
                        player_data["OversBowled"] = bowler["OversBowled"]
                        player_data["Ones"] = bowler["Ones"]
                        player_data["Twos"] = bowler["Twos"]
                        player_data["Threes"] = bowler["Threes"]
                        player_data["Fours"] = bowler["Fours"]
                        player_data["Sixes"] = bowler["Sixes"]
                        player_data["Wides"] = bowler["Wides"]
                        player_data["NoBalls"] = bowler["NoBalls"]
                        player_data["Byes"] = bowler["Byes"]
                        player_data["LegBye"] = bowler["LegBye"]
                        player_data["Wickets"] = bowler["Wickets"]
                        player_data["InningsRuns"] = bowler["InningsRuns"]
                        player_data["InningsWickets"] = bowler["InningsWickets"]
                        player_data["MatchRuns"] = bowler["MatchRuns"]
                        player_data["MatchWickets"] = bowler["MatchWickets"]
                        player_data["BBIW"] = bowler["BBIW"]
                        player_data["BBMW"] = bowler["BBMW"]
                        player_data["Maidens"] = bowler["Maidens"]
                        player_data["MaidenWickets"] = bowler["MaidenWickets"]
                        player_data["FourWickets"] = bowler["FourWickets"]
                        player_data["FiveWickets"] = bowler["FiveWickets"]
                        player_data["TenWickets"] = bowler["TenWickets"]
                        player_data["BowlingClientPlayerID"] = bowler["ClientPlayerID"]
        if player_data:
            all_rounders_data.append(player_data)

    json_str = json.dumps(all_rounders_data)

    filename = f"{team1}vs{team2}{year}.json"
    # write json string to file
    with open(filename, 'w') as f:
        f.write(json_str)
    
    print(f"All rounder data for {year} is written")

