import pandas as pd

file_B = pd.read_csv('build/store/thin_renamed.csv')

file_B.rename(columns={'Provider First Name': 'First_Name'}, inplace=True)

file_B.to_csv('build/store/thin_renamed.csv', index=False)

print("The column header has been renamed and saved to 'file_B_renamed.csv'.")
