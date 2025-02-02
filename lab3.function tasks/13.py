import random
def guess_the_number(n, cnt, name):
    print('Take a guess. \n')
    m = int(input())
    cnt += 1
    if m == n:
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
    if m > n:
        print('Your guess is too high.')
        guess_the_number(n, cnt, name)
    if m < n:
        print('Your guess is too low.')
        guess_the_number(n, cnt, name)

print('Hello! What is your name?')
name = str(input())

print(f'Well, {name}, I am thinking of a number between 1 and 20.')

cnt = 0
n = random.randint(1, 20)

guess_the_number(n, cnt, name)