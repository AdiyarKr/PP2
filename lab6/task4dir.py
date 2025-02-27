def count_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return len(lines)


filename = "e.txt"
line_count = count_lines(filename)
print(f"Number of lines in {filename} - {line_count}")