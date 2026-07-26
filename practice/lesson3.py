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
    {"name": "Sarah"}
]

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
    for key, value in counts.items():
        print(f"The following are the missing colums in the dataset {key}:{value} {bad_rows } bad rows and total {row_count} rows")


if __name__ == "__main__":

    bad_rows, row_count, counts = dataset_summary(data)
    bad_rows1, row_count1, counts1 = dataset_summary(new_data)
    bad_rows2, row_count2, counts2 = dataset_summary(malformed_data)

    data_info(bad_rows, row_count, counts)
    data_info(bad_rows1, row_count1, counts1)
    data_info(bad_rows2, row_count2, counts2)





