automobile = { "1.one wheel" : "Tyre",
               "2.two wheel" : "Scooter",
               "6.six wheel" : "Bus",
               "4.four wheel" : "car"
               }
# keys = list(automobile.keys())
#
# keys.sort()

# keys = sorted(automobile.keys())
#
# print(keys)
#
# for item in keys:
#     print ( item + " : " + automobile[item])

for item in sorted(automobile.keys()):
    print ( item + " : " + automobile[item])

print(automobile.keys())
print(automobile.values())
