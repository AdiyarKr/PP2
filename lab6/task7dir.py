def tocopyfile(orig_file, copy_file):
    with open(orig_file, "r") as orig, open(copy_file, "w") as copy:
        copy.write(orig.read())


orig_file = "orig.txt"
copy_file = "copy.txt"
tocopyfile(orig_file, copy_file)