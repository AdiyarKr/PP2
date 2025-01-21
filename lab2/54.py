thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
for x in thisdict:
  print(x)
for x in thisdict:
  print(thisdict[x])

for x, y in thisdict.items():
  print(x, y)