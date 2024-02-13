# Place code below to do the analysis part of the assignment.
import csv

def analyze_data(input_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter=' ')

        # Skip the header line
        next(reader)

        # Initialize the decades dictionary
        decades = {i: [] for i in range(1880, 2021, 10)}

        # Iterate over the rows in the file
        for row in reader:
            year = int(row[0])
            anomaly = float(row[1])

            # Find the decade for this year
            decade = year - (year % 10)

            # Add the anomaly to the appropriate decade list
            decades[decade].append(anomaly)

    # Calculate the average temperature anomaly for each decade
    for decade, anomalies in decades.items():
        average_anomaly = sum(anomalies) / len(anomalies)
        average_anomaly_f = round(average_anomaly * 9 / 5 + 32, 1)
        print(f'{decade} to {decade + 9}: {average_anomaly_f} F')

input_file = 'data/clean_data.csv'
analyze_data(input_file)