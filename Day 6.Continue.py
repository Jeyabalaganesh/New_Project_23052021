# classic = ["puffs", "Tea", "milk", "Priya", "coffee" ]
#
# for pos in range(len(classic)):
#     if classic[pos].casefold()  != "priya" :
#         continue
#     print ("The position of {0} in classic is {1}".format(classic[pos], pos ))
#
# *****************************************************************************************

a =2
b =5
sum = 0

for x in range (16):
    if x < 10:
        continue
    sum = sum + a + (b*x)

print ("The sum is {}".format(sum))
