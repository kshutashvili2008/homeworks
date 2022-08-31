arr = "nika zuka gabrieli gio saba andria daviti"

# output = ["nika1", "zuka2", "gabrieli3"]

#step1 create an array from string
splitted_arr = arr.split()

final_arr = []

for i in range(0, len(splitted_arr)):
    final_arr.append(splitted_arr[i]+str(i+1))

print(final_arr)