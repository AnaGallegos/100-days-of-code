
numbers = [1,2,3,4,5]
new_numbers = [item+1 for item in numbers]

name = "camelia"
new_name = [letter + letter.upper() for letter in name]


names = ["Alex", "Beth", "Camelia", "Alexandra", "Pete"]
short_names = [name for name in names if len(name) < 5]
upper_short_names = [name.upper() for name in names]

squared_numbers = [number **2 for number in numbers]

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)