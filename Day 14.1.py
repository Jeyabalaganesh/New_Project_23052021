automobile = { "1.one wheel" : "Tyre",
               "2.two wheel" : "Scooter",
               "6.six wheel" : "Bus",
               "4.four wheel" : "car"
}
print(automobile)
print()
print(automobile["1.one wheel"])


for item in automobile:
    print(item + " : " + automobile[item])

auto_tuple = tuple(automobile.items())
print(auto_tuple)

for item in auto_tuple:
    key,value = item
    print( key + ":" + value)

auto_dict = dict(auto_tuple)
print(auto_dict)
