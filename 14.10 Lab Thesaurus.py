# TODO: Read the word and letter from the user
word = input()
letter = input()

# TODO: Open and read the corresponding text file into a dictionary
synonyms = {}
file_name = word + ".txt"

try:
    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            for synonym_word in words:  # Use a different variable name here
                if synonym_word[0] in synonyms:
                    synonyms[synonym_word[0]].append(synonym_word)
                else:
                    synonyms[synonym_word[0]] = [synonym_word]
except FileNotFoundError:
    synonyms = {}

# TODO: Output synonyms that begin with the given letter
if letter in synonyms:
    for synonym in synonyms[letter]:
        print(synonym)
else:
    print(f"No synonyms for {word} begin with {letter}.")
