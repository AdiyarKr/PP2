import string

def gen_al_f():
    alph = string.ascii_uppercase
    for letter in alph:
        filename = f"{letter}.txt"
        with open (filename, 'w') as file:
            file.write(f"This a file {filename}")
        print(f'Creates a file {filename}')

gen_al_f()