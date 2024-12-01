import json

first_location_id_list = []
second_location_id_list = []
with open ("input.txt", "r") as file:
    for line in file:
        first_location_id_list.append(line.split()[0])
        second_location_id_list.append(line.split()[1])

sorted_list_1 = sorted(first_location_id_list)
sorted_list_2 = sorted(second_location_id_list)

total_diff = 0
print(sorted_list_1[0])
print(sorted_list_2[0])
while len(sorted_list_1) > 0:
    abcd = sorted_list_1.pop(0)
    dafg = sorted_list_2.pop(0)
    temp_diff = abs(int(abcd) - int(dafg))
    total_diff += temp_diff
    print(len(sorted_list_1))

print(total_diff)

similarity_score = 0
for location_id in first_location_id_list:
    a = 0
    for location_id2 in second_location_id_list:
        if location_id != location_id2:
            pass
        else:
            a += 1

    temp_sim_score = int(location_id) * a
    similarity_score += temp_sim_score

print(similarity_score)