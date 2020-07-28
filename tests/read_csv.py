import csv
path = r"tests\user_data.csv"
with open(path) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  next(csv_reader)

  for row in csv_reader:
    if row:
      print(row)
      