import csv

filename = 'tel_review_added.csv'
base_xlsx_idx = 256


with open(filename, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)


del rows[base_xlsx_idx-1:]

with open('new_'+filename, 'w', newline="\n", encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(rows[:base_xlsx_idx-1])
    