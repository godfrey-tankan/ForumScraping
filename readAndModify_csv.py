
import csv
import random
from datetime import datetime, timedelta
import os

input_file = 'Bulawayo Railway Museum.csv'
output_file = 'Bulawayo Railway Museum reviews.csv'

start_date = datetime(2013, 1, 1)
end_date = datetime(2023, 12, 31)

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, input_file)
output_path = os.path.join(current_dir, output_file)

with open(input_path, 'r') as input_csv, open(output_path, 'w', newline='') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    print(f"Converting CSV file: {input_path}")
    header = next(reader)
    header.append('date_of_review')
    writer.writerow(header)

    for row in reader:
        print('Processing row:', row)
        random_date = start_date + timedelta(seconds=random.randint(0, (end_date - start_date).total_seconds()))
        row.append(random_date.strftime('%Y-%m-%d'))
        writer.writerow(row)

print(f"CSV file converted successfully: {output_path}")