import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader) #pula a linha 1
    with open('new_names.csv', 'w') as new_file:
        field_names = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter = '\t')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)

