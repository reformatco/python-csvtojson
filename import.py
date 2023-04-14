import csv
import json
import os

# Define a dictionary that maps the CSV column headers to the desired output keys
header_map = {
    'name': 'title',
    'address': 'street',
    'postcode': 'post_code',
    'web': 'website',
    'social media': 'socials',
    'type': 'mtype',
    'phone': 'telephone'
}

# Set the input and output directory paths
input_dir = 'csv/'
output_dir = 'json/'

# Loop through each CSV file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        # Construct the full path to the input and output files
        input_path = os.path.join(input_dir, filename)
        basename = os.path.splitext(filename)[0] + '.json'
        output_path = os.path.join(output_dir, basename)

        # Open the CSV file
        with open(input_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            # Get the keys from the first row and map them to the desired output keys
            keys = [header_map.get(header, header) for header in next(csvreader)]

            # Initialize an empty list to store the data
            data = []

            # Loop through each row in the CSV file
            for row in csvreader:
                # Check if the row is blank (i.e., contains no values)
                if not any(row):
                    continue  # Skip to the next row

                # Map the row data to the desired output keys
                row_data = {header_map.get(keys[i], keys[i]): row[i] for i in range(len(keys))}
                
                # Create an array called socials with the first item
                if 'socials' in row_data:
                    row_data['socials'] = [row_data['socials']]
                    
                # Add the row data to the list of data
                data.append(row_data)

        # Write the data to a JSON file in the output directory
        with open(output_path, 'w') as jsonfile:
            json.dump(data, jsonfile)

        print(f"Data from {filename} written to {output_path}")
