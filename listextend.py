countries = ["India", "USA", "UK", "Italy"]

print("List Before Appending Item")
print(countries)

tuple1 = ("Japan", "China", "France")
countries.extend(tuple1)
print("\nList After Appending Tuple using extend")
print(countries)

list1 = [19, 17, 39, 55]
countries.extend(list1)
print("\nList After Appending List sing extend")
print(countries)

countries.extend((11.5, 19.2))
print("\nList After Appending 11.5, 19.2 using extend")
print(countries)
