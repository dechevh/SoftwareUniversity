journal = input().split(", ")
command = input()

inventory = list(journal)

while command != "Craft":
    different_commands = command.split(" - ")

    action = different_commands[0]
    item = different_commands[1]

    if action == "Collect":
        if item in inventory:
            pass
        else:
            inventory.append(item)
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        tokens = item.split(":")
        old_item = tokens[0]
        new_item = tokens[1]

        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)
    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()
    if command == "Craft!":
        break

print(", ".join(inventory))
# [print(f"{x}", sep=", ") for x in inventory]
# [print(*x, sep=", ") for x in inventory]
