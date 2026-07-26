import csv
def dataset_summary(dataset):
    row_count = 0
    bad_rows = 0
    counts = {}

    
    columns = []

    for row in dataset:
        if isinstance(row, dict):
            for key in row.keys():
                if key not in columns:
                    columns.append(key)


    for data in dataset:
        row_count += 1

        if not isinstance(data, dict):
            bad_rows += 1
            continue

        for column in columns:
            if column not in data or data[column] is None:
                counts[column] = counts.get(column, 0) + 1

    return bad_rows, row_count, counts

def data_info(bad_rows, row_count, counts):
    if not counts:
        print(f"No missing values found. {bad_rows} bad rows and total {row_count} rows")
    else:
        for key, value in counts.items():
            print(
                f"The following are the missing columns in the dataset {key}: {value}. "
                f"{bad_rows} bad rows and total {row_count} rows"
            )



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
        bad_rows, row_count, counts = dataset_summary(data)
        data_info(bad_rows, row_count, counts)
    
    return data



