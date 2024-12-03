import json

# safe_rows = []
# unsafe_rows = []
# abc = 0
# with open ("input.txt", "r") as file:
#     for line in file:
#         abc += 1
#         # print(abc)

#         line_as_list = line.split()
#         temp_line_as_list = line.split()
#         list_length = len(line_as_list)
#         a = 0
#         list_of_diffs = []
#         while len(list_of_diffs) + 1 < list_length:
#             position0 = int(line_as_list[0])
#             position1 = int(line_as_list[1])
#             diff = position0 - position1
#             list_of_diffs.append(diff)
#             line_as_list.pop(0)
            
#         negative_count = 0
#         positive_count = 0
#         for difference in list_of_diffs:
#             if difference == 0 or abs(difference) > 3:
#                 unsafe_rows.append(temp_line_as_list)
#                 break
#             elif difference > 0:
#                 positive_count += 1
#             elif difference < 0:
#                 negative_count += 1

#         if positive_count > 0 and negative_count > 0:
#             unsafe_rows.append(temp_line_as_list)
#         else:
#             safe_rows.append(temp_line_as_list)


# unique_safe_rows = set(tuple(row) for row in safe_rows)
# unique_unsafe_rows = set(tuple(row) for row in unsafe_rows)

# print(f"For Part 1, the number of safe rows: {abc - len(unique_unsafe_rows)}")

def all_same_sign(lst):
    if all(x > 0 and x < 4 for x in lst):
        return "All positive and less than 4"
    elif all(x < 0  and x > -4 for x in lst):
        return "All negative and greater than -4"
    else:
        return "Mixed signs or too large a gap"




safe_rows = []
unsafe_rows = []
row_diffs = []
list_of_lines = []
abc = 0
with open ("input.txt", "r") as file:
    for line in file:
        abc += 1
        # print(abc)
        line_as_list = line.split()
        temp_line_as_list = line.split()
        list_of_lines.append(temp_line_as_list)
        list_length = len(line_as_list)
        a = 0
        list_of_diffs = []
        while len(list_of_diffs) + 1 < list_length:
            position0 = int(line_as_list[0])
            position1 = int(line_as_list[1])
            diff = position0 - position1
            list_of_diffs.append(diff)
            line_as_list.pop(0)
        
        row_diffs.append(list_of_diffs)


# print(row_diffs[0])
# print(list_of_lines[0])

# a = 0
for row in row_diffs:
    # print(f"This is item # {a} in the list of rows.")
    temp_message = f"{all_same_sign(row)}"
    if temp_message != "Mixed signs or too large a gap":
        safe_rows.append(row)
    else:
        # print(list_of_lines[a])
        unsafe_rows.append(list_of_lines[a])

    # a += 1



for row in unsafe_rows:
    while len(row) > 1:
        pos0 = int(row[0])
        pos1 = int(row[1])
        if pos0 - pos1 > 0 and pos0 - pos1 < 4:
            change_type = "Positive and safe"
            print(change_type)
        elif pos0 - pos1 < 0 and pos0 - pos1 > -4:
            change_type = "Negative and safe"
            print(change_type)
        else:
            print(f'This line is unsafe somewhere between {pos0} and {pos1}')

        

        row.pop(0)


        


# unique_safe_rows = set(tuple(row) for row in safe_rows)
# unique_unsafe_rows = set(tuple(row) for row in unsafe_rows)

# print(f"For Part 2, the number of safe rows: {len(safe_rows)}")
# print(f"For Part 2, the number of unsafe rows: {len(unique_unsafe_rows)}")
            