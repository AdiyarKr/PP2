def list_to_file(file_path, d):
    with open(file_path, 'w') as file:
        for item in d:
            file.write(str(item) + ' ')

mylist = [1, 2, 3, 4, 5]
file_path = "mydoc.txt"
list_to_file(file_path, mylist)
print(f"Now lis is file with name {file_path}")