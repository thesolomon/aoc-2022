input_file = "input.txt"
input = open(input_file, 'r')
games = input.readlines()

rock = 1
paper = 2
scissors =3
win = 6
lose = 0
draw =3

outcomes = {
    "A X": rock+draw, #rock v rock
    "A Y": paper+win, #rock v paper
    "A Z": scissors+lose, #rock v scissors
    "B X": rock+lose, #paper v rock
    "B Y": paper+draw, #paper v paper
    "B Z": scissors+win, #paper v scissors
    "C X": rock+win, # scissors v rock
    "C Y": paper+lose, # scissors v paper
    "C Z": scissors+draw, # scissors v scissors
}

outcomes2 = {
    "A X": scissors+lose, #rock lose
    "A Y": rock+draw, #rock draw
    "A Z": paper+win, #rock win
    "B X": rock+lose, #paper lose
    "B Y": paper+draw, #paper draw
    "B Z": scissors+win, #paper win
    "C X": paper+lose, # scissors lose
    "C Y": scissors+draw, # scissors draw
    "C Z": rock+win, # scissors win
}

def play_game(mapping):
    score = 0
    for game in games:
        game = game.strip()
        score += mapping[game]
    print(score)

play_game(outcomes)
play_game(outcomes2)
