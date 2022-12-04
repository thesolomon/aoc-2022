#yon is 4 in Japanese, in case you didn't know

def p1():
    filey_boi = "aoc-2022/dayyon/input.txt"
    input_boi = open(filey_boi, 'r')
    parsed_bois = input_boi.readlines()

    pair_count = 0
    for boi in parsed_bois:
        boi = boi.strip()
        e1_assignment, e2_assignment = boi.split(",")
        e1_start, e1_end = [int(x) for x in e1_assignment.split("-")]
        e2_start, e2_end = [int(x) for x in e2_assignment.split("-")]
        if e1_start > e2_start:
            if e1_end <= e2_end:
                pair_count +=1
                print(f"{e1_assignment},{e2_assignment}")
        elif e1_start < e2_start: 
            if e1_end >= e2_end:
                pair_count +=1
                print(f"{e1_assignment},{e2_assignment}")
        elif e1_start == e2_start:
            pair_count +=1
            print(f"{e1_assignment},{e2_assignment}")

    print(pair_count)

def p2():
    filey_boi = "aoc-2022/dayyon/input.txt"
    input_boi = open(filey_boi, 'r')
    parsed_bois = input_boi.readlines()

    pair_count = 0
    for boi in parsed_bois:
        boi = boi.strip()
        e1_assignment, e2_assignment = boi.split(",")
        e1_start, e1_end = [int(x) for x in e1_assignment.split("-")]
        e2_start, e2_end = [int(x) for x in e2_assignment.split("-")]
        if e1_start > e2_end:
            continue
        elif e1_end < e2_start:
            continue
        else:
            pair_count +=1
    print(pair_count)

p1()
p2()