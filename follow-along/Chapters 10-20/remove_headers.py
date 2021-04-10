'''
Follow along project from ch. 16 of automate the 
boring stuff which uses the csv module to remove
the first row headers from a csv file.

This project does not remove headers from csv files
in subfolders of the specified directory.
'''
import os, csv

os.chdir('follow-along/Chapters 10-20/remove headers test')
os.makedirs('header removed', exist_ok=True)

for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'): continue
    print(f'removing header from {csv_filename}...')

    csv_rows = []
    csv_file_obj = open(csv_filename)
    reader_obj = csv.reader(csv_file_obj)
    
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue
        csv_rows.append(row)
    csv_file_obj.close()

    new_csv = open(os.path.join('header removed', csv_filename), 'w', newline='')
    csv_writer = csv.writer(new_csv)
    for row in csv_rows:
        csv_writer.writerow(row)
    new_csv.close()

print('Complete!')