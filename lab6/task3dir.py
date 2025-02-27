import os

def test_exists(path):
    if os.path.exists(path):
        print("Path exists.")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exist.")

path1 = "/Users/adiyarkarim/Desktop/pp2/pp2/lab6/dir_and_files/task4.py"
test_exists(path1)