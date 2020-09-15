targets = list(map(int, input().split('|')))
command = input()

points = 0

while command != "Gave over":
    if command == "Reverse":
        pass
    else:
        tokens = command.split("@")
        action = tokens[0]
        start_index = int(tokens[1])
        length = int(tokens[2])

        wanted_index = 0

        if action == "Shoot Left":
            index = start_index
            for i in range(index, length):
                wanted_index = i
                if index == length:
                    index = 0
                index -= 1

            print(wanted_index)

        elif action == "Shoot Right":
            index = length - 1

            command = input()
            if command == "Gave over":
                break

print()

# # simple way to do the task
# if index == length
#     index = 0
#
# -------------------
#
# index = 0
# length = 5
#
# for i in range(10):
#     print(f"{index % length}")
#     index +=1 #depends if we want to start from left or right so it could be -1

# sum() - returns the sum of the list we provides
