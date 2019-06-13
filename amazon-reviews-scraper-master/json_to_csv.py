
import json
import csv
import pandas


# f = open('B01MYU349G.json')
# data = json.load(f)
# f.close()

#f = csv.writer(open('data.csv', 'wb+'))
# use encode to convert non-ASCII characters
#for item in data:
   # f.writerow([item['body'], item['rating']])
#f.writerows(data)
pandas.read_json('B01MYU349G.json').to_csv('pandas.csv')
