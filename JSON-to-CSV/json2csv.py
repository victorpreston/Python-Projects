import json
import csv
import os

print("\nWelcome to the JSON to CSV converter")

class Converter:

    def converter(self, json_file_path, csv_file_name):
        global data
        if json_file_path == 1:
            try:
                with open(json_file_path, 'r') as f1:
                    data = json.load(f1)
            except:
                print("File not found")
                print("Try creating a new json file")
                return
        
        if json_file_path == 2:
            f = open("input.json",'x')
            f.close()
            file = "notepad input.json"
            os.system(file)
            f1 = open("input.json",'r')
            data = json.load(f1)

        f2 = open(csv_file_name, 'w', newline="")
        writer_object = csv.writer(f2)
        writer_object.writerow(data[0].keys())

        for row in data:
            writer_object.writerow(row.values())
        f2.close()

        choice = input("Do you want open the converted file? (y/n): ")
        while choice not in ['y','n']:
            print("Invalid choice")
            choice = input("Do you want open the converted file? (y/n): ")
        if choice == 'y':
            os.system(f'start "excel" {csv_file_name}')

json2csv = Converter()

json_file_path = int(input("""
Press (1) to Open an existing json file
Press (2) to Create a new json file and Enter your data
Choose any one: """))

csv_file_name = input("Name your CSV file: ")+".csv"

json2csv.converter(json_file_path, csv_file_name)