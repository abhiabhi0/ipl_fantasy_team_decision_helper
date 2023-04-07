from itertools import combinations

# define the player names
batsmen = ['a1', 'a2', 'a3']
bowlers = ['b9', 'b10', 'b11']

# create a list of all possible combinations of 1 or more batsmen
batsmen_combinations = []
for i in range(1, len(batsmen)+1):
    batsmen_combinations.extend(combinations(batsmen, i))

# create a list of all possible combinations of 1 to 3 bowlers
bowlers_combinations = []
for i in range(1, 4):
    bowlers_combinations.extend(combinations(bowlers, i))

# loop through each combination of batsmen and bowlers
for b_comb in batsmen_combinations:
    for bo_comb in bowlers_combinations:
        # check if there is only one performing batsman
        if sum([b in b_comb for b in batsmen]) == 1:
            # check if there are 2 or 3 performing bowlers
            if sum([bo in bo_comb for bo in bowlers]) > 1:
                print(f"Batsmen: {b_comb}, Bowlers: {bo_comb}")
