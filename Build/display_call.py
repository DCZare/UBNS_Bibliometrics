import csv

def get_headers_and_first_row_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)  
        first_row = next(reader, None) 
        return headers, first_row
