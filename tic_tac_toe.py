PLAYER_X = 'X'
PLAYER_O = 'O'
DRAW = 'Draw'
SPACE = '_'


def print_field(field):
    print("---------")
    print("|", field[0], field[1], field[2], "|")
    print("|", field[3], field[4], field[5], "|")
    print("|", field[6], field[7], field[8], "|")
    print("---------")


def is_coordinate(data):
    if len(data) != 2:
        print("You should enter numbers!")
        return False
    for num in data:
        if not num.isdigit():
            print("You should enter numbers!")
            return False
        elif int(num) < 1 or 3 < int(num):
            print("Coordinates should be from 1 to 3!")
            return False
    return True


def ask_coordinates(coordinate):
    result = False
    while result is False:
        coordinate = input("Enter the coordinates: > ").split()
        result = is_coordinate(coordinate)
    return coordinate


def cell_number(coord):
    return int(coord[0]) - 1 + (3 - int(coord[1])) * 3



def check_winner(field):
	line_wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
				(0, 3, 6), (1, 4, 7), (2, 5, 8),
				(0, 4, 8), (2, 4, 6))
	wins = ''
	for line in line_wins:
		if field[line[0]] == field[line[1]] == field[line[2]] != SPACE:
			wins = field[line[0]]
			return wins
	if SPACE not in field:
		return DRAW
	return None


def next_step(player):
	if player == PLAYER_X:
		return PLAYER_O
	else:
		return PLAYER_X



def main():
	field = list("_________")
	print_field(field)
	coordinates = []
	step = PLAYER_X
	winner = None
	while not winner:
		coordinates = ask_coordinates(coordinates)
		cell = cell_number(coordinates)
		if field[cell] == '_':
			field[cell] = step
			step = next_step(step)
			print_field(field)
		else:
			print("This cell is occupied! Choose another one!")
		winner = check_winner(field)
	print(winner + ' wins' if winner != DRAW else DRAW)
