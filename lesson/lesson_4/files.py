# colors = ["red", "blue", "6574", "yellow"]
# data = open("file.txt", "a", encoding= "utf-8")
# data.writelines(colors)
# data.close

# with open("file.txt", "w") as data:
#     data.write("line 1\n")
#     data.write("line 3\n")
# print(56)

path = "file.txt"
data = open("file.txt", "r")
for line in data:
    print(line)
data.close()
