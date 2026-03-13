import random

# Player Pool with Performance Tiers (1=Core, 2=Rotation, 3=Variance)
players = [
    {"name": "J Bumrah", "team": "IND", "role": "BOWL", "tier": 1},
    {"name": "S Yadav", "team": "IND", "role": "BAT", "tier": 1},
    {"name": "H Pandya", "team": "IND", "role": "AR", "tier": 1},
    {"name": "M Santner", "team": "NZ", "role": "BOWL", "tier": 1},
    {"name": "R Ravindra", "team": "NZ", "role": "AR", "tier": 1},
    {"name": "S Samson", "team": "IND", "role": "WK", "tier": 2},
    {"name": "A Patel", "team": "IND", "role": "AR", "tier": 2},
    {"name": "A Singh", "team": "IND", "role": "BOWL", "tier": 2},
    {"name": "D Mitchell", "team": "NZ", "role": "BAT", "tier": 2},
    {"name": "M Chapman", "team": "NZ", "role": "BAT", "tier": 2},
    {"name": "L Ferguson", "team": "NZ", "role": "BOWL", "tier": 2},
    {"name": "F Allen", "team": "NZ", "role": "BAT", "tier": 3},
    {"name": "S Dube", "team": "IND", "role": "AR", "tier": 3},
    {"name": "T Varma", "team": "IND", "role": "BAT", "tier": 3},
    {"name": "M Henry", "team": "NZ", "role": "BOWL", "tier": 2},
    {"name": "I Kishan", "team": "IND", "role": "WK", "tier": 2},
    {"name": "V Chakaravarthy", "team": "IND", "role": "BOWL", "tier": 3},
    {"name": "T Seifert", "team": "NZ", "role": "WK", "tier": 3},
    {"name": "C McConchie", "team": "NZ", "role": "AR", "tier": 3},
    {"name": "G Phillips", "team": "NZ", "role": "BAT", "tier": 2}
]

def generate_performance_team():
    team = []
    # Force include 4 Core players
    core = [p for p in players if p['tier'] == 1]
    team.extend(random.sample(core, 4))
    
    # Add 5 Rotation players
    rotation = [p for p in players if p['tier'] == 2]
    team.extend(random.sample(rotation, 5))
    
    # Add 2 High Variance players for differential
    variance = [p for p in players if p['tier'] == 3]
    team.extend(random.sample(variance, 2))
    
    return team

def generate_40_lineups():
    unique_teams = []
    seen_combinations = set()
    
    while len(unique_teams) < 40:
        team = generate_performance_team()
        # Sort names to check for duplicates
        team_names = tuple(sorted([p['name'] for p in team]))
        
        if team_names not in seen_combinations:
            seen_combinations.add(team_names)
            
            # Assign Multipliers based on performance tiers
            captain = random.choice([p['name'] for p in team if p['tier'] == 1])
            vice_captain = random.choice([p['name'] for p in team if p['name'] != captain])
            
            unique_teams.append({
                "team_id": len(unique_teams) + 1,
                "players": list(team_names),
                "captain": captain,
                "vice_captain": vice_captain
            })
            
    return unique_teams

# Execute and print
lineups = generate_40_lineups()
for lineup in lineups:
    print(f"Team {lineup['team_id']}: C: {lineup['captain']}, VC: {lineup['vice_captain']}")
    print(f"Players: {', '.join(lineup['players'])}\n")