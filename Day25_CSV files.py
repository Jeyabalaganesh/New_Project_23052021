import csv

# with open("sample.csv", "r", newline="") as csv_file:
#     data = csv.reader(csv_file, delimiter="!", skipinitialspace=True, quotechar=",")
#
#     for item in data:
#         # print(item)
#         # print(item[0], item[1], item[2], item[3], item[4])
#         print(item[1])


data_header = ["sl", "Name", "Age"]
scholar_data = [
                ["1", "Jb", "29"],
                ["2", "jbg", "28"],
                ["3", "bala", "25"]
                ]

with open ("scholars.csv", "w") as csv_file:
    data = csv.writer(csv_file)
    data.writerow(data_header)
    data.writerows(scholar_data)
