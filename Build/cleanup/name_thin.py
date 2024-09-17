import pandas as pd

def thin():

    csv_file_path = 'build/data/expanded_file_A.csv'

    df = pd.read_csv(csv_file_path)

    print("Column Headers:")
    for column in df.columns:
        print(column)

    print('Lets-a-go!')

    columns_to_keep = ['Last_Name', 'Middle_Initial', 'First_Name', 'work_title'] 

    df = pd.read_csv(csv_file_path, usecols=columns_to_keep)

    df.to_csv('build/data/thin_Bulk_2.csv', index=False)

    print('------------------')
    print('Done :)')
    print('------------------')

    print("Column Headers:")
    for column in df.columns:
        print(column)


def no_Mid():

    csv_file_path = 'build/data/thin_Bulk_2.csv'

    df = pd.read_csv(csv_file_path)

    print("Column Headers:")
    for column in df.columns:
        print(column)

    print('Lets-a-go!')

    columns_to_keep = ['Last_Name', 'First_Name', 'work_title']  

    df = pd.read_csv(csv_file_path, usecols=columns_to_keep)

    df.to_csv('build/data/thin_Bulk_3.csv', index=False)

    print('------------------')
    print('Done :)')
    print('------------------')

    print("Column Headers:")
    for column in df.columns:
        print(column)

no_Mid()