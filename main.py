import csv
import os


def main(file_path, header_names, delimiter, expected_num_columns):
    file_present = check_file_exists(file_path)
    if not file_present:
        print("File not found")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        csv_table = list(csv.reader(f, delimiter=delimiter))

    header_check = check_file_header(csv_table, header_names)
    if not header_check:
        return False

    num_columns = check_file_columns(csv_table, expected_num_columns)
    if num_columns:
        print("File is valid")
        return True
    else:
        print("Expected number of columns and actual number of columns in file do not match")
        return False


def check_file_exists(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        return False


def check_file_header(csv_table, header_names):
    has_header = False
    if header_names is None:  # If header names are not given explicitly
        has_header = False
    header_name = header_names.strip()
    if len(header_name) > 0:
        has_header = True
    else:
        has_header = False

    if not any(cell.isdigit() for cell in csv_table[0]):  # checking if there is header row present in data or not
        is_header = True
        if has_header:
            print("File already has header")
    else:
        is_header = False
        if not has_header:
            print("File doesn't have any header")

    if has_header != is_header:
        return True
    else:
        return False


def check_file_columns(csv_table, expected_num_columns):
    num_columns = len(csv_table[0])
    print(num_columns)
    if num_columns == expected_num_columns:
        return True
    else:
        return False


main('D:\Codnix\X_FAM.txt', header_names=" ", delimiter='\t', expected_num_columns=31)
