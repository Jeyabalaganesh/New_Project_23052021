dom_animals = { "cow"  : "gives milk",
                "goat" : "gives meat",
                "cat"  : "eats rat",
                "dog"  : "always bark"
}

print(dom_animals)
# for item in sorted(dom_animals.keys()):
#     print (item + " : " + dom_animals[item])

dom_animals["horse"] = "we can ride"

print(dom_animals)

dom_animals["Cow".casefold()] = "has 2 horns"

print(dom_animals)

del dom_animals["Goat".casefold()]

print(dom_animals)

dom_animals.clear()
print(dom_animals)
