# Data collection scripts

This folder contains 4 Python scripts for data collection and one script for combining the collected data. The data collection scripts are named 'request_pollution_data_{location}.py', and their usage is given below:

python \<script name>.py \<username> \<password>

In order to gather the data you need a different account on pulse.eco, for each of the following cities Skopje, Kumanovo, Kichevo, Tetovo. After creating an account on the website pass your credentials as shown above to start gathering the data. Currently the scripts are set up to gather data from 01.01.2020 to 20.10.2020, for every hour, but can be modified to span another time period. After gathering the data for each location and pollutant, we combine this data using the combine_data.py script. This outputs 8 .csv files, for each of the measurement stations respectively (5 measurement stations in Skopje, 1 in Tetovo, 1 in Kumanovo and 1 in Kichevo). These files contain data for all of the pollutants, but there is a huge number of NaNs. The files with the gathered data from these scripts are located in the 'Data/Pre, raw/pollution/' folder.
