import os

def list_direc(p):
    print([x.name for x in os.scandir(path=p) if x.is_dir()])

def list_files(p):
    print([x.name for x in os.scandir(path=p) if x.is_file()])

def list_direc_files(p):
    print([x.name for x in os.scandir(path=p)])

path = str(input())
list_direc(path)
list_files(path)
list_direc_files(path)