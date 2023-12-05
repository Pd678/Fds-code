cricket = []
badminton = []
football = []

num_cricket = int(input("Number of students who play cricket:"))
for _ in range(num_cricket):
    name = str(input("Enter name of cricket player:"))
    cricket.append(name)
print("Cricket players:", cricket)

num_badminton = int(input("Number of students who play badminton:"))
for _ in range(num_badminton):
    name = str(input("Enter name of badminton player:"))
    badminton.append(name)
print("Badminton players:", badminton)

num_football = int(input("Number of students who play football:"))
for _ in range(num_football):
    name = str(input("Enter name of football player:"))
    football.append(name)
print("Football players:", football)

def both_sports(cricket_list, badminton_list):
    common_players = [player for player in cricket_list if player in badminton_list]
    print("Students who play both cricket and badminton:", common_players)

both_sports(cricket, badminton)

def either_sport(cricket_list, badminton_list):
    combined_players = list(set(cricket_list).union(set(badminton_list)))
    print("Students who play either cricket or badminton:", combined_players)

either_sport(cricket, badminton)

def neither_sport(cricket_list, football_list, badminton_list):
    neither_players = [player for player in football_list if player not in cricket_list and player not in badminton_list]
    print("Students who play neither cricket nor badminton:", neither_players)

neither_sport(cricket, football, badminton)

def cricket_and_football(cricket_list, football_list, badminton_list):
    special_players = [player for player in cricket_list if player in football_list and player not in badminton_list]
    print("Students who play cricket and football but not badminton:", special_players)

cricket_and_football(cricket, football, badminton)
