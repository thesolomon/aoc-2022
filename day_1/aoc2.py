from collections import Counter

input_file = "test.txt"
input = open(input_file, 'r')
elves = input.readlines()
elf_count = 1
calories_carried = {"elf_1":0}
highest_calories = 0

for line in elves:
  if line == '\n':
    elf_count +=1
    calories_carried[f'elf_{elf_count}'] = 0
    continue
  calories_carried[f'elf_{elf_count}'] += int(line)

top = Counter(calories_carried)

for swol_elf_bois in top.most_common(3):
    highest_calories += swol_elf_bois[1]

print(highest_calories)