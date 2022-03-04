import json
import csv

with open('data_json.json') as json_file:
    data = json.load(json_file)

user_data = data['users']
# label = user_data.keys()
# headers = user_data["1645505582797"].keys()

csv_file = open('data_csv.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
cnt = 0

for us in user_data:
    if cnt == 0:
        label = user_data[us].keys()
        csv_writer.writerow(label)
        cnt += 1
    csv_writer.writerow(user_data[us].values())

csv_file.close()