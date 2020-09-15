single_numbers = input().split(" ")
sum_numbers = 0

top_numbers = []

for x in single_numbers:
    sum_numbers += int(x)

average_value = sum_numbers / len(single_numbers)

for x in single_numbers:
    if int(x) > average_value:
        top_numbers.append(str(x))

best_five = list((sorted(top_numbers)))

res = best_five[-5:]
print(" ".join(res))
