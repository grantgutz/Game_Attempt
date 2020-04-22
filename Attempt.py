def xp_check(level, skill_points, xp,):
    while xp >= 100:
        level = level + 1
        skill_points = skill_points + 1 
        xp = xp - 100
        return (skill_points, xp, level)

def skill_point_assignment (skill_points, strength, agility, luck, health):
    while skill_points > 1:
        x= int(input("You have " + str(skill_points) + " skill points avalible. Enter a 1 to incress strength, 2 to incress agility, 3 to incress luck, or 4 to incress health: "))
        skill_points = skill_points - 1
        if x == 1:
            strength = strength + 1
            print (("You know have ") + str(strength) + (" total strength."))
        elif x == 2:
            agility = agility + 1
            print (("You know have ") + str(agility) + (" total agility."))
        elif x == 3:
            luck = luck + 1
            print (("You know have ") + str(luck) + (" total luck."))
        elif x == 4:
            health = health + 3
            print (("You know have ") + str(health) + (" total health."))

    if skill_points == 1:
        x = int(input("You have " + str(skill_points) + " skill point avalible. Enter a 1 to incress strength, 2 to incress agility, 3 to incress luck, or 4 to incress health: "))
        skill_points = skill_points - 1
        if x == 1:
            strength = strength + 1
            print (("You know have ") + str(strength) + (" total strength."))
        elif x == 2:
            agility = agility + 1
            print (("You know have ") + str(agility) + (" total agility."))
        elif x == 3:
            luck = luck + 1
            print (("You know have ") + str(luck) + (" total luck."))
        elif x == 4:
            health = health + 3
            print (("You know have ") + str(health) + (" total health."))
    if skill_points == 0:
        print (("You have no remaining skill points and a total of ") + str(strength) + (" strength, ") + str(agility) + (" agility, ") + str(luck) + (" luck, and ") + str(health) + (" health."))
    return (skill_points, strength, agility, luck)

#Player Stats 


    
#Enemy stats 
def skeleton_stats(enemy_strength, enemy_health, enemy_agility):
    enemy_strength == 1
    enemy_health == 3
    enemy_agility == 1
    print (enemy_agility)
    return (enemy_strength, enemy_health, enemy_agility, )

skeleton_stats()

#Combate
def combat_system():
    #Player attacks
    enemy_health = enemy_health - strength
    if enemy_health >= 0: 
        print(("You attack the ") + str(enemy_name) + (" dealing ")+ str(strength) + (" damage. It has ") + str(enemy_health) + ("remaining. "))
    else:
        print(("You attack the ") + str(enemy_name) + (" dealing ")+ str(strength) + (" damage. It dies"))











