dogs = ["Roger", 1, "syd", True]
dogs[2] = "John"
print(dogs[-1])
print(dogs[:2])

print(len(dogs))
dogs.append("item")
dogs.extend(["judah", "dorime"])
dogs += ["ameno",'latire']

dogs.remove("Roger")
dogs.pop() #remove the last item

print(dogs)

items = ['Ben','dell','HP']

items.sort(key=str.lower)

