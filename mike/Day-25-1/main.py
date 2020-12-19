import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_count_gray= len(data[data['Primary Fur Color'] == 'Gray'])
squirrel_count_red = len(data[data['Primary Fur Color'] == "Cinnamon"])
squirrel_count_black = len(data[data['Primary Fur Color'] == 'Black'])

print(squirrel_count_black)
print(squirrel_count_red)
print(squirrel_count_gray)