from profiler import dataset_summary, data_info, read_data, check_data



if __name__ == "__main__":

    data2 = read_data('practice/data/data2.csv')
    data = read_data('practice/data/data.csv')

    check_data(data)
    check_data(data2)
