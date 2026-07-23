data = [
 {"name": "mike", "school": "absu", "city": None},
 {"name": "bryan", "school": "absu", "city": "abia"}
]


new_data = [
    {"name": "Alice", "school": "NOUN", "city": "Abuja"},
    {"name": "John", "school": "UNILAG", "city": "Lagos"},
    {"name": "Mary", "school": "UI", "city": "Ibadan"},
    {"name": "Peter", "school": "UNN", "city": "Enugu"},
    {"name": "Grace", "school": "ABU", "city": "Zaria"}
]


malformed_data = [
    {"name": "James", "school": "LASU"},
    {"name": "Sarah", "city": "Kano"},
    "This is not a dictionary",
    12345
]

def dataset_summary(dataset):
    row_count = 0
    bad_rows = 0
    missing_name = 0
    missing_school =0
    missing_city = 0

    for data in dataset:
        row_count += 1
    
 
        try:
            

            name = data["name"]
            school = data["school"]
            city = data["city"]

            

            if name is None:
                missing_name += 1
            if school  is None:
                missing_school += 1
            if city is None:
                missing_city += 1
            
            


                
                
        except KeyError:
            print("This is not the right Key")
            bad_rows += 1
        except TypeError:
            print("Dataset does not have the type")
            bad_rows += 1
        
       
    


                
    return missing_city, missing_name, missing_school, row_count, bad_rows


def data_info(missing_city, missing_name, missing_school, row_count, bad_rows):
    print(f"There are {missing_name} missing names, and {missing_school} missing schools and  {missing_city} missing cities in this dataset, with total row is {row_count} and {bad_rows} bad rows")


city_res, name_res, school_res, total_rows, bad_rows = dataset_summary(data)
city_re, name_re, school_re, total, bad_row = dataset_summary(new_data)
city, name, school, totals, bad = dataset_summary(malformed_data)

data_info(city_res, name_res, school_res, total_rows, bad_rows)
data_info(city_re, name_re, school_re, total, bad_row)
data_info(city, name, school, totals, bad)





