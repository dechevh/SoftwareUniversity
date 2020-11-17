sting_rooms = input().split("|")

health = 100
bitcoins = 0
dead = False
best_room = 0
latest_monster = ""
counter = len(sting_rooms)

while not dead:
    if counter == 0:
        break

    for x in sting_rooms:
        each_room = x.split(" ")
        command = each_room[0]
        number = int(each_room[1])
        best_room += 1
        counter -= 1

        if command == "potion":
            if health + number > 100:
                healed = 100 - health
                health = 100
            else:
                health += number
                healed = number

            print(f"You healed for {healed} hp.")
            print(f"Current health: {health} hp.")

        elif command == "chest":
            bitcoins += number
            print(f"You found {number} bitcoins.")

        else:
            health -= number
            latest_monster = command

            if health <= 0:
                dead = True
                print(f"You died! Killed by {latest_monster}.")
                print(f"Best room: {best_room}")
                break
            else:
                print(f"You slayed {command}.")

if not dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
