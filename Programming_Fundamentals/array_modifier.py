initial_array = list(map(int, input().split(" ")))
array = initial_array

res = list()
command = input()

while command != "end":
    if command == "decrease":
        decreased_array = [x - 1 for x in array]
        res = decreased_array
    else:
        tokens = command.split(" ")
        action = tokens[0]
        first_element = int(tokens[1])
        second_element = int(tokens[2])

        if action == "swap":
            array[first_element], array[second_element] = array[second_element], array[first_element]
        elif action == "multiply":
            new_value = array[first_element] * array[second_element]
            array[first_element] = new_value

    command = input()

res_final = list(map(lambda x: str(x), res))

print(", ".join(res_final))
