file_name = input("Enter file name: ")

try:
    file = open(file_name, "r")

    content = file.read()

    words = content.split()

    print("Total number of words:", len(words))

    file.close()

except FileNotFoundError:
    print("Error! File not found.")
