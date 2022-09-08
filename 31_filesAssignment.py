with open("file.txt") as file:
    file_data = file.read()
    file_data = file_data.replace("cows", "ducks")
    file_data = file_data.replace("moo", "quack")

with open("file.txt",'a') as file_write:
    file_write.writelines("\n" + file_data)

