Stats = []

for i in range(0,3):
    name = input()
    attack = int(input())
    defense = int(input())
    character =[name, (attack, defense)]
    Stats.append(character)

for i in range(0,3):
    print(str(Stats[i][0]))
    print(str(Stats[i][1][0]))
    print(str(Stats[i][1][1]))
print(Stats)
max_attack_Stats = Stats[0]
max_defense_Stats = Stats[0]

for character in Stats:
    if character[1][0] > max_attack_Stats[1][0]:
        max_attack_Stats = character
    if character[1][1] > max_defense_Stats[1][1]:
        max_defense_Stats = character

print("Ataque " + max_attack_Stats[0] + " " + str(max_attack_Stats[1][0]))
print("Defesa " + max_defense_Stats[0] + " " + str(max_defense_Stats[1][1])) 