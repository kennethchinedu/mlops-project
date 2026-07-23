data = [
 {"name": "mike", "school": "absu", "city": None},
 {"name": "bryan", "school": "absu", "city": "abia"}
]


new_data = [
    {"name": "chioma", "school": "unilag", "city": "lagos"},
    {"name": "emeka", "school": "unn", "city": None},
    {"name": None, "school": "uniben", "city": "benin"},
    {"name": "tunde", "school": None, "city": "ibadan"},
    {"name": "amina", "school": "abu", "city": "aria"}
]



def dataset_summary(dataset):
    row_count = 0
    missing_name = 0
    missing_school =0
    missing_city = 0

    for data in dataset:
        row_count += 1
        for key, value  in data.items():
            # print(f"{key}:{value} ")

            if key == "name" and value is None:
                missing_name += 1
            elif key == "school" and value is None:
                missing_school += 1
            elif key == "city" and value is None:
                missing_city += 1
            
                
    return missing_city, missing_name, missing_school, row_count


def data_info(missing_city, missing_name, missing_school, row_count):
    print(f"There are {missing_name} missing names, and {missing_school} missing schools and  {missing_city} missing cities in this dataset, with total row is {row_count}")


city_res, name_res, school_res, total_rows = dataset_summary(data)
city_re, name_re, school_re, total = dataset_summary(new_data)

data_info(city_res, name_res, school_res, total_rows)
data_info(city_re, name_re, school_re, total)





