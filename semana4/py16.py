import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data= csv.reader(data_file)

    print(csv_data)
    next(csv_data)
    next(csv_data)
    #print(list(csv_data))
    for line in csv_data:
        line = line[0][1:].split(';')
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")


html_output += f'<p>There are currently {len(names)} public contributors. Thank You !</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)