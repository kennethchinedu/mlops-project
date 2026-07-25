import csv
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




def read_data(datapath):

    dataset = []

    try:

        with open(datapath, newline='') as csvfile:
            
            reader = csv.DictReader(csvfile)
            for row in reader:
                for key, value in row.items():
                    if value == '':
                        row[key] = None
                  
                dataset.append(row)

        return dataset  

    except FileNotFoundError:
        print(f"The data can't be found in this path {datapath}")
        return dataset
    
    
   
def check_data(data):

    if data == []:
        print("Dataset returned an empty list")

    else:
        city_res, name_res, school_res, total_rows, bad_rows = dataset_summary(data)
        data_info(city_res, name_res, school_res, total_rows, bad_rows)
    
    return data



