import pandas as pd

input_file = "data/stitch_Endpoint.csv"  
mid_file = "data/oops_all_dupes.csv"
output_file = "data/no_dupe.csv" 

df = pd.read_csv(input_file)

dupe_groups = df.groupby(['First_Name', 'Last_Name']).filter(lambda x: x['NPI'].nunique() > 1)

dupe_groups.to_csv(mid_file, index=False)

print('-----------------------------')
print('Duplicates with conflicting NPIs Identified')
print('-----------------------------')

df_cleaned = df.groupby(['First_Name', 'Last_Name']).filter(lambda x: x['NPI'].nunique() == 1)

print('-----------------------------')
print('Conflicting Duplicates Removed')
print('-----------------------------')

df_cleaned.to_csv(output_file, index=False)

print(f"Duplicates Stored. Cleaned data saved to {output_file}.")
