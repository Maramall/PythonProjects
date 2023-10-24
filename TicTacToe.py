#tic tac toe
	
def input_names():
	name1 = input("Первый игрок, введи своё имя: ")
	if len(name1) > 64:
		name1 = input("Пхах, слишком длинное имя, давай короче: ")
	if len(name1) > 64:
		name1 = input("Что, с первого раза непонято? Введи имя хотя бы меньше 100 символов: ")
	if len(name1) > 100:
		name1 = 'player1'
	name2 = input("Второй игрок, введи своё имя: ")
	if len(name2) > 64:
		name2 = 'player2'
	return name1, name2
	
def naming_players(player1, player2):
	players = {player1 : 'X', player2 : 'O'}
	return players

def output_cell(values):

	a = [' ┌———————————┐',' | ' + values[0] + ' | ' + values[1] + ' | ' + values[2] + ' |',' |———┼———┼———|',' | ' + values[3] + ' | ' + values[4] + ' | ' + values[5] + ' |',' |———┼———┼———|',' | ' + values[6] + ' | ' + values[7] + ' | ' + values[8] + ' |',' └———————————┘']

	for i in range(7):
		for j in range(14):
			print(a[i][j], end="")
		print("")

def input_coords(player):

	print(f"{player}, введи строку и столбец: ")
	coords = input()

	try:
		coords = int(coords)
	except ValueError:
		x, y = input_coords(player)
		return x, y  	
	x = coords // 10
	y = coords % 10
	if x > 3 or y > 3 or x < 1 or y < 1:
		print("неправильно, ", end = "")
		x, y = input_coords(player)
		return x, y
	return x, y

def next_values(values, player, symb):
	x, y = input_coords(player)
	if values[(x-1)*3+y-1] == ' ':
			values[(x-1)*3+y-1] = symb
			return True
	else: 
			print(f"на {x} {y} уже что-то поставили")
			next_values(values, player, symb)
			
def win_or_not(values):
	if (values[0] ==  values[1] and values[1] == values[2] and values[0] != ' ') or (values[0] ==  values[4] and values[4] == values[8] and values[0] != ' ') or (values[2] ==  values[4] and values[4] == values[6] and values[2] != ' ') or (values[3] ==  values[4] and values[4] == values[5] and values[3] != ' ') or (values[6] ==  values[7] and values[7] == values[8] and values[6] != ' ') or (values[0] ==  values[3] and values[3] == values[6] and values[0] != ' ') or (values[2] ==  values[5] and values[5] == values[8] and values[2] != ' '):
		return True
	return False
#==============================================================================================================================================

values = [' ']*9
players = input_names()
dictplayers = naming_players(players[0], players[1])
output_cell(values)
#x, y = input_coords(players[0])
for i in range(9):
	next_values(values, players[i%2], dictplayers[players[i%2]])
	output_cell(values)
	if win_or_not(values):
		print(players[i%2], " победил!")
		break
	if i == 8:
		print("Draw")

'''
a = 
 ┌———————————┐ 
 | X | X | X | // a[1]
 |———┼———┼———|  
 | x | O | x | // a[3]
 |———┼———┼———|
 | x | O | x | // a[5]
 └———————————┘

'''
