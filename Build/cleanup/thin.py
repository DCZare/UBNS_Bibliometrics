import pandas as pd

csv_file = 'build/store/npidata_pfile_20050523-20240811.csv'

print('Lets-a-go!')

columns_to_keep = ['NPI', 'Provider Last Name (Legal Name)', 'Provider First Name', 'Provider First Line Business Mailing Address', 'Provider Business Mailing Address City Name']  # Replace with your desired column names

df = pd.read_csv(csv_file, usecols=columns_to_keep)

df.to_csv('build/data/thin__city_NPI.csv', index=False)

print('Done :)')
