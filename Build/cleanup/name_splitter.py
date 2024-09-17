import pandas as pd

file_A = pd.read_csv('build/store/NS_Bulk_2023.csv')

print('File Found')
print('Begining Modification')

file_A[['First_Name', 'Middle_Initial', 'Last_Name']] = file_A['author_name'].str.split(expand=True, n=2)

file_A['Last_Name'] = file_A.apply(lambda row: row['Middle_Initial'] if pd.isna(row['Last_Name']) else row['Last_Name'], axis=1)
file_A['Middle_Initial'] = file_A.apply(lambda row: None if row['Last_Name'] == row['Middle_Initial'] else row['Middle_Initial'], axis=1)

file_A = file_A.drop(columns=['author_name'])

file_A.to_csv('build/data/expanded_file_A.csv', index=False)

print("The expanded DataFrame has been saved to 'expanded_file_A.csv'.")

