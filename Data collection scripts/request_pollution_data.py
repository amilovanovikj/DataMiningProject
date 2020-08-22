import requests
from getpass import getpass
import sys
from datetime import datetime
from datetime import timedelta
counter = 0
import time
url = 'https://kichevo.pulse.eco/rest/dataRaw'
#'https://skopje.pulse.eco/rest/dataRaw?sensorId=1001&type=pm10&from=2017-03-15T02:00:00%2b01:00&to=2017-03-19T12:00:00%2b01:00
#'https://skopje.pulse.eco/rest/dataRaw?sensorId=1001&type=pm10&from=2017-03-15T02%3A00%3A00%252b01%3A00&to=2017-03-19T12%3A00%3A00%252b01%3A00
# date_from = sys.argv[1]
# date_to = sys.argv[2]
#2018-12-31
#2020-02-24
date_from_string = '2018-12-31'
date_to_string = '2019-01-07'

with open('pollution_kicevo.csv','w') as file:
    file.write('sensorId')
    file.write('\t')
    file.write('stamp')
    file.write('\t')
    file.write('type')
    file.write('\t')
    file.write('position')
    file.write('\t')
    file.write('value')
    file.write('\n')

while True:
    time.sleep(0.1)
    parameters = {
            'sensorId' : '4001',
            'type' : 'pm10',
            'from' : f'{date_from_string}T23:00:00%2b01:00',
            'to' : f'{date_to_string}T23:00:00%2b01:00'
    }

    params_str = '&'.join("%s=%s" % (k,v) for k,v in parameters.items())

    response = requests.get(url, auth = ('aleksej38','leunovo12'),params = params_str)


    if response.status_code == 200:

        raw_data = response.json()

        with open('pollution_kicevo.csv','a') as file:
            for i in range(0,len(raw_data)):
                counter = 0
                for value in raw_data[i].values():
                    counter+=1
                    file.write(value)
                    if counter == 5:
                        file.write('\n')
                    else:
                        file.write('\t')
    else:
        print(response.url)
        print(response.status_code)

    date_from =  datetime.strptime(date_from_string,'%Y-%m-%d').date()
    date_to = datetime.strptime(date_to_string,'%Y-%m-%d').date()

    date_from =  date_from + timedelta(days=7)
    date_to =  date_to + timedelta(days=7)

    date_from_string = date_from.strftime('%Y-%m-%d')
    date_to_string = date_to.strftime('%Y-%m-%d')
    print(date_from_string)
    if date_from_string == '2020-03-02':
        print('top')
        break



