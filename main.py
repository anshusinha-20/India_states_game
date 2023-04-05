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
# print(data["temp"])

# """converting the data to dictionary format"""
# dataDict = data.to_dict()
# print(dataDict)

# """converting the data to a list"""
# tempList = data["temp"].to_list()
# sum = 0
# for temp in tempList:
#     sum += temp
# avgTemp = sum / len(tempList)
# print(round(avgTemp, 2))

# avgTemp = sum(tempList) / len(tempList)
# print(round(avgTemp, 2))

# """getting the avg temperature"""
# print(
#     round(
#         data["temp"].mean(), 2
#     )
# )
#
# """getting the maximum value from the data's temp column"""
# print(
#     data["temp"].max()
# )
#
# """getting the data in a column"""
# print(
#     data.condition
# )

# """getting the data in a row"""
# print(
#     data[data.day == "Monday"]
# )

# print(
#     data[data.temp == data.temp.max()]
# )

# """getting the condition of a single row"""
# monday = data[data.day == "Monday"]
# print(monday.condition)

# """creating a dataframe from scratch"""
# dataDict = {
#     "students": ["Anuragini", "Arup", "Bibek", "Aadarsh"],
#     "age": [19, 20, 21, 21]
# }
#
# data2 = pandas.DataFrame(dataDict)
# print(data2)
#
# """converting the obtaines data to csv format"""
# print(
#     data2.to_csv()
# )