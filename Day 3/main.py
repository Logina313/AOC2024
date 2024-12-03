import re

with open ("input.txt", "r") as file:
    input_string = file.read()

match_pattern = r"mul\(\d{1,3},\d{1,3}\)"
do_dont_pattern = r"do\(\)|don't\(\)"

part1_matches = re.findall(match_pattern, input_string)
part1_answer = 0
for match in part1_matches:
    numbers = match.replace("mul(","").replace(")","").split(",")
    part1_answer += int(numbers[0]) * int(numbers[1])

print(f"Part 1 Answer: {part1_answer}")

part2_matches = re.finditer(rf"{do_dont_pattern}|{match_pattern}", input_string)

multiply = True
part2_answer = 0

for thing in part2_matches:
    text = thing.group(0)
    if text == "do()":
        multiply = True
    elif text == "don't()":
        multiply = False
    elif "mul" in text and multiply:
        numbers = text.replace("mul(", "").replace(")", "").split(",")
        part2_answer += int(numbers[0]) * int(numbers[1])

print(f"Part 2 Answer: {part2_answer}")

