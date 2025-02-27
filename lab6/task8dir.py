import os

def delete_file(path):
    if not os.path.exists(path):
        print("The path does not exist")
        return

    if not os.access(path, os.W_OK):
        print("No write access to the file")
        return

    os.remove(path)
    print(f"File at {path} deleted successfully")


your_path = str(input())
delete_file(your_path)