import csv
import json

with open("data/input.csv") as file:
    reader = csv.DictReader(file)
    data = list(reader)          # Convert to a list of dicts


with open("data/output.json", "w") as file:
    json.dump(data, file)        # Write data directly to a file


with open("data/output.json", "w") as file:
    json_str = json.dumps(data)  # Convert data to str
    file.write(json_str)         # Write str to file
