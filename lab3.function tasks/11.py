def polindrom(st):
    reve = st[::-1]
    if reve == st:
        return 'Polindrom'
    return 'Not plindrom'
s = input()
print(polindrom(s))