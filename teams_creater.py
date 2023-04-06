import itertools

team_a_top_order = ['simran', 'Dhawan', 'RajPak']
team_a_lower_order = ['Jitesh', 'Curan', 'Raza']
team_b_top_order = ['Jaiswal', 'Butler', 'Samson']
team_b_lower_order = ['Padikal', 'Parag', 'Hetmayar']

player_performance = {
    'simran': 0,
    'Dhawan': 0,
    'RajPak': 0,
    'Jitesh': 0,
    'Curan': 0,
    'Raza': 0,
    'Jaiswal': 0,
    'Butler': 0,
    'Samson': 0,
    'Padikal': 0,
    'Parag': 0,
    'Hetmayar': 0
}

def create_teams(scenario):
    team_a_selected = []
    team_b_selected = []
    for i in range(len(team_a_top_order)):
        if scenario[i] == 2:
            if player_performance[team_a_top_order[i]] == 1 and player_performance[team_a_top_order[i+1]] == 1:
                team_a_selected.append(team_a_top_order[i])
                team_a_selected.append(team_a_top_order[i+1])
                break
        else:
            if player_performance[team_a_lower_order[i]] == 1 and player_performance[team_a_lower_order[i+1]] == 1:
                team_a_selected.append(team_a_lower_order[i])
                team_a_selected.append(team_a_lower_order[i+1])
                break
    
    for i in range(len(team_b_top_order)):
        if scenario[i+3] == 2:
            if player_performance[team_b_top_order[i]] == 1 and player_performance[team_b_top_order[i+1]] == 1:
                team_b_selected.append(team_b_top_order[i])
                team_b_selected.append(team_b_top_order[i+1])
                break
        else:
            if player_performance[team_b_lower_order[i]] == 1 and player_performance[team_b_lower_order[i+1]] == 1:
                team_b_selected.append(team_b_lower_order[i])
                team_b_selected.append(team_b_lower_order[i+1])
                break

    return team_a_selected + team_b_selected

scenarios = list(itertools.product([1, 2], repeat=6))

for i, scenario in enumerate(scenarios, 1):
    team_a = ", ".join(team_a_top_order) + ", " + ", ".join(team_a_lower_order)
    team_b = ", ".join(team_b_top_order) + ", " + ", ".join(team_b_lower_order)
    scenario_teams = create_teams(scenario)
    print(f"Scenario {i}: {team_a} vs {team_b} => {scenario_teams}") 
