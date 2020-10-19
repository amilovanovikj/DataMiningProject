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
if len(sys.argv) < 3:
    print("ERROR: Invalid number of arguments: {}.\nPlease provide the username and password for the pulse.eco API.".format(len(sys.argv) - 1))
    exit()

username = sys.argv[1]
password = sys.argv[2]

pollutants = ['AQI', 'CO', 'CO2', 'NO2', 'O3', 'PM10', 'PM25', 'SO2']
for pollutant in pollutants:
    date_from_string = '2019-12-31'
    date_to_string = '2020-01-07'

    with open('{}_kicevo.csv'.format(pollutant),'w') as file:
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
                'type' : pollutant.lower(),
                'from' : f'{date_from_string}T23:00:00%2b01:00',
                'to' : f'{date_to_string}T23:00:00%2b01:00'
        }

        params_str = '&'.join("%s=%s" % (k,v) for k,v in parameters.items())

        response = requests.get(url, auth = (username, password),params = params_str)

        if response.status_code == 200:

            raw_data = response.json()

            with open('{}_kicevo.csv'.format(pollutant),'a') as file:
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
        print(pollutant + ": " +  date_from_string)
        if date_from_string == '2020-10-20':
            print('DONE!')
            break