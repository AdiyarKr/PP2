
def un_list(mylist):
    uniq = []
    for x in mylist:
        if x not in uniq:
            uniq.append(x)
    return uniq

mylistt = input().split()
print(un_list(mylistt))