# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# """imported csv module"""
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

"""imported pandas module"""
import pandas

"""using pandas module to read a csv file"""
data = pandas.read_csv("weather_data.csv")
print(data["temp"])