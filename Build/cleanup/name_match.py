import pandas as pd

file_A = pd.read_csv('build/data/thin_Bulk_3.csv')  
file_B = pd.read_csv('build/store/thin_renamed.csv')  

def preprocess_names(df, name_columns):
    for col in name_columns:
        df[col] = df[col].str.strip().str.title()
    return df

file_A = preprocess_names(file_A, ['First_Name', 'Last_Name'])
file_B = preprocess_names(file_B, ['First_Name', 'Last_Name'])

print('Preprocessing Complete')
print('Commencing Stitching')

merged_df = pd.merge(file_A, file_B, on=['First_Name', 'Last_Name'], how='inner')

merged_df.to_csv('build/data/stitch_Endpoint.csv', index=False)

print("The merged DataFrame with NPI_ID has been saved to 'stitch_Endpoint.csv'.")
