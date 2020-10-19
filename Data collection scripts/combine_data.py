import numpy as np
import pandas as pd

locations = ['centar', 'gazi_baba', 'karpos', 'kicevo', 'kumanovo', 'lisice', 'miladinovci', 'tetovo']
pollutants = ['AQI', 'CO', 'CO2', 'NO2', 'O3', 'PM10', 'PM25', 'SO2']

for loc in locations:
    data = pd.DataFrame(columns=['time'])
    for p in pollutants:
        df = pd.read_csv('./{}_{}.csv'.format(p, loc), sep='\t', parse_dates=['stamp'])
        df['stamp'] = pd.to_datetime(df['stamp'], utc=True).astype(int)
        df['stamp'] = df['stamp'].apply(lambda t: t//1000000000)
        new_df = pd.DataFrame(columns=['time', p])
        new_df['time'] = df['stamp']
        new_df[p] = df['value']
        data = data.merge(new_df, how='outer', on='time')
    data = data[['AQI', 'CO', 'CO2', 'NO2', 'O3', 'PM10', 'PM25', 'SO2', 'time']]
    data.to_csv('./pollution_report_{}.csv'.format(loc), index=False)