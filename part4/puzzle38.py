from ict_skills import skills1

# Define the wish-set
wishlist = {'Python', 'SQL', 'Java', 'Blockchain'}

num_teams = 0

# Iterate through all possible combinations of 3
programmers = list(skills1.keys())
num_programmers = len(programmers) #50

for i in range(num_programmers): #start bij [0]
    for j in range(i + 1, num_programmers): #start bij [1]
        for k in range(j + 1, num_programmers): #start bij [2]
            
            programmer1_skills = skills1[programmers[i]]
            programmer2_skills = skills1[programmers[j]]
            programmer3_skills = skills1[programmers[k]]

            # add skills of programmer to team's skills
            team_skills = set()
            for skill in programmer1_skills:
                team_skills.add(skill)
            for skill in programmer2_skills:
                team_skills.add(skill)
            for skill in programmer3_skills:
                team_skills.add(skill)

            # Now just check if the team has all the desired skills and voila
            if wishlist.issubset(team_skills):
                num_teams += 1

print("Number of different teams:", num_teams)
