count_arr = [0] * 4

for _ in range(3):
    symptom, temp = input().split()
    temp = int(temp)
    if (symptom == 'Y') and (temp >= 37):
        count_arr[0] += 1
    elif (symptom == 'N') and (temp >= 37):
        count_arr[1] += 1
    elif (symptom == 'Y') and (temp < 37):
        count_arr[2] += 1
    else:
        count_arr[3] += 1
if count_arr[0] >= 2:
    count_arr.append('E')

print(" ".join(map(str, count_arr)))
