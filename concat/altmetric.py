import pyaltmetric
from pyaltmetric import Altmetric
import csv

dois = ('10.1016/j.wneu.2018.08.242', '10.1111/epi.13298')

a = Altmetric()

citations = list(map(a.doi, dois))

fieldnames = set()
for citation in citations:
    fieldnames.update(citation.keys())

fieldnames = sorted(fieldnames)

csv_file_path = 'concat/citations.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for citation in citations:
        row = {fieldname: citation.get(fieldname, '') for fieldname in fieldnames}
        writer.writerow(row)

print(f"Citations have been written to {csv_file_path} in CSV format.")

