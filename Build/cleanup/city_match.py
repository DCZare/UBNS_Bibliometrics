import pandas as pd

def merge_csv_files(file_a, file_b):
  """Merges two CSV files based on matching First_Name, Last_Name, and city_Name.

  Args:
    file_a: Path to the first CSV file.
    file_b: Path to the second CSV file.

  Returns:
    A merged DataFrame containing the data from both files.
  """

  df_a = pd.read_csv(file_a)
  df_b = pd.read_csv(file_b)

  def preprocess(df):
    df['First_Name'] = df['First_Name'].str.strip().str.title()
    df['Last_Name'] = df['Last_Name'].str.strip().str.title()
    df['city_Name'] = df['city_Name'].str.strip().str.title()
    return df

  df_a = preprocess(df_a)
  df_b = preprocess(df_b)

  merged_df = pd.merge(df_a, df_b, on=['First_Name', 'Last_Name', 'city_Name'], how='inner')

  return merged_df

file_a_path = 'build/data/thin_city_NPI.csv'
file_b_path = 'build/data/city_match_out.csv'

merged_df = merge_csv_files(file_a_path, file_b_path)

merged_df.to_csv('build/data/merged_output.csv', index=False)