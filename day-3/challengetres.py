def problem_one():
    input_file = "aoc-2022/day-3/file.txt"
    input = open(input_file, 'r')
    games = input.readlines()

    sum = 0
    order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for game in games:
        game = game.strip()
        length = int(len(game)/2)
        sack1 = set(game[:length])
        sack2= set(game[length:])
        item = (sack1 & sack2).pop()
        sum += order.find(item)+1
    print(f"final sum part 1: {sum}")

def problem_two():
    input_file = "aoc-2022/day-3/file.txt"
    input = open(input_file, 'r')
    games = input.readlines()

    sum = 0
    sets = []
    order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(len(games)):
        sets.append(games[x].strip())
        if x%3 == 2:
            item = (set(sets[0]) & set(sets[1]) & set(sets[2])).pop()
            sum += order.find(item)+1
            sets.clear()
    print(f"final sum part 2: {sum}")

problem_one()
problem_two()



