students = [

]

missing_age = 0
missing_name = 0
missing_city = 0
row_count = 0 

for  data in students:

    print(data.keys())

    # age = data["age"]
    # city = data["city"]
    # name = data["name"]

    # row_count += 1

    # if age is None:
    #     missing_age += 1
    # if city is None:
    #     missing_city += 1
    # if name is None:
    #     missing_name += 1




print(f"The age is missing {missing_age} values, city is missing {missing_city} values and name {missing_name} values, total row is {row_count}")