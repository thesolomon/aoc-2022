input_file = "test.txt"
input = open(input_file, 'r')
elves = input.readlines()
elf_count = 1
calories_carried = {"elf_1":0}

for line in elves:
  if line == '\n':
    elf_count +=1
    calories_carried[f'elf_{elf_count}'] = 0
    continue
  calories_carried[f'elf_{elf_count}'] += int(line)

highest_calories = max(calories_carried.values())
print(highest_calories)