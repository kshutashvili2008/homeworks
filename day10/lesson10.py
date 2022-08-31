# full_name="nikoloz ksutashvili"

# i = 0
# for char in full_name:
#     print(i,"indexze-ზე დგას",char)
#     i += 1

full_name="nikoloz kshutashvili"

i = 0

for char in full_name:
    if char not in "aeiou":
        print("თანხმოვანი detected at psition" + str(i) + "და ეს თანხმოვანია" + char)
    i += 1


