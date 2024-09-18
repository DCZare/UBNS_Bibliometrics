import pyaltmetric
import os
from pyaltmetric import Altmetric
import csv

cwd = os.getcwd()

print(cwd)

i = 1

input_csv_file_path = os.path.join(cwd, 'Build/data/doi_split_single_work_output.csv')

#dois = ('10.1016/j.wneu.2018.08.242', '10.1111/epi.13298')
dois = []
original_rows = []

with open(input_csv_file_path, 'r') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    if 'work_doi' not in fieldnames:
        raise ValueError("The 'doi' column is missing from file_a.csv")
        print('Error')
        
    
    for row in reader:
        dois.append(row['work_doi'])
        original_rows.append(row)
        #print(f'Completed: {row["work_title"]}')
        #print(dois)


a = Altmetric()

citations = []
for doi in dois:
    citation = a.doi(doi)
    if citation is not None:
        citations.append(citation)
        print(f'{i} Found: {doi}')
        i = i+1
    else:
        print(f"{i}: No citation data found for DOI: {doi}")
        i = i+1


fieldnames = set()
for citation in citations:
    #print(citation)
    fieldnames.update(citation.keys())

fieldnames = sorted(fieldnames)

csv_file_path = 'Build/concat/outputs/citations.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for citation in citations:
        row = {fieldname: citation.get(fieldname, '') for fieldname in fieldnames}
        writer.writerow(row)

print(f"Citations have been written to {csv_file_path} in CSV format.")

