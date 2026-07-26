from profiler import dataset_summary, data_info, read_data, check_data
import sys


if __name__ == "__main__":
    try:
        data = read_data(sys.argv[1])
        check_data(data)

    except IndexError:
        print("Error: Missing CSV file path.")
        print("Usage: python app.py <path_to_csv>")
        print("Example: python app.py practice/data/data.csv")
