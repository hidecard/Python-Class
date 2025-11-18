# File Handling in Python (I/O)
# Examples for txt, csv, json files with modes: r (read), w (write), a (append), r+ (read/write)

import csv
import json

# 1. Text File Handling
def text_file_examples():
    # Writing to a text file (mode 'w')
    with open('example.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a text file.\n")

    # Reading from a text file (mode 'r')
    with open('example.txt', 'r') as file:
        content = file.read()
        print("Read content:", content)

    # Appending to a text file (mode 'a')
    with open('example.txt', 'a') as file:
        file.write("Appended line.\n")

    # Read and write (mode 'r+')
    with open('example.txt', 'r+') as file:
        existing = file.read()
        file.write("New line added.\n")
        print("After r+:", existing + "New line added.\n")

# 2. CSV File Handling
def csv_file_examples():
    # Writing to CSV (mode 'w')
    with open('example.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', 25, 'NYC'])
        writer.writerow(['Bob', 30, 'LA'])

    # Reading from CSV (mode 'r')
    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("CSV Row:", row)

    # Appending to CSV (mode 'a')
    with open('example.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Charlie', 35, 'Chicago'])

    # Read and write CSV (mode 'r+') - Note: r+ for CSV needs careful handling
    with open('example.csv', 'r+') as file:
        reader = csv.reader(file)
        rows = list(reader)
        print("Existing CSV rows:", rows)
        # Append in r+ mode
        file.seek(0, 2)  # Go to end
        writer = csv.writer(file)
        writer.writerow(['David', 40, 'Miami'])

# 3. JSON File Handling
def json_file_examples():
    data = {'name': 'John', 'age': 30, 'city': 'NYC'}

    # Writing to JSON (mode 'w')
    with open('example.json', 'w') as file:
        json.dump(data, file)

    # Reading from JSON (mode 'r')
    with open('example.json', 'r') as file:
        loaded_data = json.load(file)
        print("Loaded JSON:", loaded_data)

    # Appending to JSON - JSON doesn't support append directly; rewrite
    with open('example.json', 'r') as file:
        existing = json.load(file)
    existing['new_key'] = 'new_value'
    with open('example.json', 'w') as file:
        json.dump(existing, file)

    # Read and write JSON (mode 'r+')
    with open('example.json', 'r+') as file:
        existing = json.load(file)
        existing['updated'] = True
        file.seek(0)
        json.dump(existing, file)

# Run examples
if __name__ == "__main__":
    print("Text File Examples:")
    text_file_examples()
    print("\nCSV File Examples:")
    csv_file_examples()
    print("\nJSON File Examples:")
    json_file_examples()
