"""Temporary file which edited the original list of English words."""

with open(r"Python\11.3\txt_files\user_word_list.txt", "r") as f:
    lines = f.readlines()

with open(r"Python\11.3\txt_files\user_word_list.txt", "w") as f:
    for line in lines:
        if len(line.strip("\n")) == 5:
            f.write(line)

with open(r"Python\11.3\txt_files\user_word_list.txt", "r") as f:
    lines = f.readlines()

letter_set = set()
with open(r"Python\11.3\txt_files\single_letter_list.txt", "w") as f:
    for line in lines:
        for letter in line:
            letter_set.add(letter)
        if len(letter_set) == 6:
            f.write(line)
        letter_set.clear()

with open(r"Python\11.3\txt_files\wordle_word_list.txt", "r") as f:
    lines = f.readlines()

with open(r"Python\11.3\txt_files\wordle_word_list.txt", "w") as f:
    for line in lines:
        for letter in line:
            letter_set.add(letter)
        if len(letter_set) == 6:
            f.write(line)
        letter_set.clear()
