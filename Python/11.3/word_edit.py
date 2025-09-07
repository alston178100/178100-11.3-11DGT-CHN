"""Temporary file which edited the original list of English words."""

with open(r"Python\11.3\txt_files\user_word_list.txt", "r") as f:
    lines = f.readlines()
with open(r"Python\11.3\txt_files\user_word_list.txt", "w") as f:
    for line in lines:
        if len(line.strip("\n")) == 5:
            f.write(line)