import csv
from lesson3 import dataset_summary, data_info




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
    
    
data2 = read_data('practice/data/data2.csv')
data = read_data('practice/data/data.csv')
   
def check_data(data):

    if data == []:
        print("Dataset returned an empty list")

    else:
        city_res, name_res, school_res, total_rows, bad_rows = dataset_summary(data)
        data_info(city_res, name_res, school_res, total_rows, bad_rows)
    
    return data

if __name__ == "__main__":

    check_data(data)
    check_data(data2)
