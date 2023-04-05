from decision_helper import calculate_data

print("Update most_runs_2023.json and Update most_wickets_2023.json file")
print("Make sure data file, for players playing in today's match is present")
print("Then proceed further")

team1 = input("Enter team1 name")
team2 = input("Enter team2 name")
team1_vs_team2_file = input("Enter file name where players playing in today's match, data is present. For eg. DCvsGT.json")

calculate_data(team1, team2, team1_vs_team2_file)