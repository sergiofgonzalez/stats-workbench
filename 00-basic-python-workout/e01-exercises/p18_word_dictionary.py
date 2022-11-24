word_dictionary = {
    "acting": "someone who does a job for a short time while the person who usually does that job is not there",
    "buzzer": "an electrical device that makes a buzzing noise and is used for signalling",
    "daft": "silly, foolish",
    "flakey": "prone to break down, unreliable",
}

while True:
    word = input("Please type the word to search (Enter to exit): ")
    if word == "":
        break
    else:
        if word in word_dictionary:
            print(f"{word}:\n{word_dictionary[word]}\n")
        else:
            print(f"{word} definition is not available in our dictionary\n")

print("-- done!")
