file_path = r"C:\Users\178100\Documents\178100-11.3-11DGT-CHN\Python\11.3-Assessment\wordle_word_list.txt"

with open(file_path, "r") as file:
    content = file.read()

modified_content = content.replace('",', " ")
modified_content_2 = content.replace('"', "")

with open(file_path, "w") as file:
    file.write(modified_content)
    file.write(modified_content_2)