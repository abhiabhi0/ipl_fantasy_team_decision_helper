from decision_helper import calculate_data
from all_rounder_handler import merge_data
from api_handler import fetch_data_from_server

print("Update most_runs_2023.json and Update most_wickets_2023.json file")
print("Make sure data file, for players playing in today's match is present")
print("Then proceed further")

team1 = input("Enter team1 name: ")
team2 = input("Enter team2 name: ")
match_num = input("Enter match number from fantasy.ipl: ")

most_wickets_2023_url = 'https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/107-mostwickets.js?callback=onmostwickets&_=1680615188201'
most_wickets_2023_filename = 'most_wickets_2023.json'
most_runs_2023_url = 'https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/107-toprunsscorers.js?callback=ontoprunsscorers&_=1680598985722'
most_runs_2023_filename = 'most_runs_2023.json'
todays_team_url = 'https://fantasy.iplt20.com/daily/services/feed/players?lang=en&gamedayId='+match_num+'&announcedVersion=04032023184908'

team1_vs_team2_filename = f"{team1}vs{team2}.json"

fetch_data_from_server(most_wickets_2023_url, most_wickets_2023_filename)
fetch_data_from_server(most_runs_2023_url, most_runs_2023_filename)
# fetch_data_from_server(todays_team_url, team1_vs_team2_filename)

for year in [2022, 2023]:
    merge_data(year, team1, team2, team1_vs_team2_filename)
    
calculate_data(team1, team2, team1_vs_team2_filename)