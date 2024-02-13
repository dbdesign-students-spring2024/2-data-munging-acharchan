# Place code below to do the munging part of this assignment.
import os

# Set the input file URL
input_file_url = 'https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt'

# Create platform-agnostic file path
platform_agnostic_file_path = os.path.join('data', 'raw_data.txt')

# Download and save the file
import urllib.request
urllib.request.urlretrieve(input_file_url, platform_agnostic_file_path)

def munge_data(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        # Write the header line
        file.write(lines[0].strip() + '\n')

        # Skip the lines with notes
        for line in lines[1:]:
            if line.startswith('*'):
                continue
            if line.strip() == '':
                continue
            if line.startswith('188'):
                # This is a line with column headings, skip it
                continue
            # Write the cleaned line to the output file
            file.write(line.strip() + '\n')

input_file = platform_agnostic_file_path
output_file = 'data/clean_data.csv'
munge_data(input_file, output_file)