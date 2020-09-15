all_books = input().split("&")
command = input()

collection = list(all_books)

while command != "Done":
    tokens = command.split(" | ")
    action = tokens[0]

    if action == "Add Book":
        book_name = tokens[1]
        if book_name in collection:
            pass
        else:
            # ls.insert(0, "new")
            collection.insert(0, book_name)
    elif action == "Take Book":
        book_name = tokens[1]
        if book_name in collection:
            collection.remove(book_name)
    elif action == "Swap Books":
        first_book = tokens[1]
        second_book = tokens[2]
        if first_book in collection and second_book in collection:
            a, b = collection.index(first_book), collection.index(second_book)
            collection[a], collection[b] = collection[b], collection[a]
    elif action == "Insert Book":
        book_name = tokens[1]
        collection.append(book_name)
    elif action == "Check Book":
        index = int(tokens[1])
        if index <= len(collection):
            print(collection[index])
        else:
            pass

    command = input()

print(", ".join(collection))
