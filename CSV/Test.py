import csv

header = []
counter = 0

# Use with keyword to handle opening / closing the file
with open('partnerize.csv') as file:

    # csvreader = csv.reader(file)
    # header = next(csvreader)
    
    # DictReader will parse each row in the file into a dictionary (key - value pairs)
    # It handles the header row automatically
    reader = csv.DictReader(file)

    for row in reader:
        # wrap with int to convert string to int type
        # changed the column index
        if int(row["price"]) > 50:
            counter += 1

print(counter)
