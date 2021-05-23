sports_equip = [
    ["Cricket",
    [
        "Bat",
        "Ball",
        "Pad",
        "Spam",
    ]],
    ["Football",
    [
        "ball",
        "Spam",
        "Goal keaper",
        "Peanalty",
    ]],
    ["Shuttle",
    [
        "Feather",
        "Raquet",
        "Service",
    ]]
]

for item in sports_equip:
    print(item[0])
    for i in item[1]:
        print("items are {0}".format(i))

print()
print()

