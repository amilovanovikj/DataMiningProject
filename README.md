# Folder Structure:

- The Data folder consists of 2 subfolders: 'Post, combined' and 'Pre, raw' and the 'Data info' file.
    - The 'Pre, raw' folder consists of two subfolders: 'polllution' and 'weather', where each contains the sutiable reports for each of the municipalities. These datasets are raw and don't have any preprocessing done on them. The pollution datasets are retrieved from pulse.eco API and the weather datasets are retrieved from the DarkSky API.
    - The 'Post, combined' folder consists of three subfolders: 'pollution', 'weather' and 'combined'. The pollution and weather folders contain reports which are results of the 'DataAggregationPipeline' notebook from the 'Data preprocessing' notebooks folder and the combined folder contains combined reports (weather+pollution) for each of the municipalities.
    - The 'Data info' file contains information for each of the attributes of both reports alongside some other useful information.
- The 'Notebooks' folder contains notebooks for each separate subject concerning the project. The notebooks are split into 3 different subfolders: 'Data preprocessing', 'EDA and clustering' and 'Model evaluation'.
    - The Data preprocessing folder contains the notebooks:
	    - DataAggregationPipeline - notebook used as pipeline for aggregating and joining the weather and pollution datasets of all municipalities. This notebook is used to generate the combined(weather+pollution) datasets and also provides minimal required preprocessing steps. The pre-processing of the pollution reports contains of:
            1. Making the time column an hourly index of the dataframe; 
            1. Fixing typos in all columns (some values contain random dots and aren't read properly - we fix this to get more data);
            1. Casting categorical data to numeric and leaving the values which can't be cast as NaNs to deal with them in the PreprocessingPipeline notebook;
            1. Removing duplicate times(rows with same index);
            1. Removing rows with PM10>1000 or PM10<0 and interpolating up to maximum of 1 missing value of PM10 using a 'linear' interpolation method; 
            1. removing all rows with NaN values for the PM10 cell. 
            The preprocessing of the weather reports contains of: 
            1. Dropping the icon column; 
            1. Replacing the NaN values for precipType, precipAccumulation and cloudCover columns with their theoretical NaN values;
            1. Interpolating the pressure columns up to maximum of 3 missing values;
            1. One-hot encoding each categorical variable
            Finally the notebook combines both of these preprocessed reports into a single report. The notebook also has a section for an example procedure	for the center municipality. We can use these section to test out more ideas for the data aggregation/joining procedure alongside the minimal preprocessing used.
	    - Feature engineering ideas and proposals and pipeline - notebook used for testing feature engineering ideas and proposals. The notebook also offers a pipeline	where the proposed feature engineering can be ran on all the combined reports for each municipality. Ideas so far:
            1. Lagging features;
            1. Stat features like mean/median of certain time frames for imputing means;
            1. Cov analysis
	    - PreprocessingPipeline - notebook for preprocessing of the combined datasets. The notebook offers a pipeline where every preprocessing step should be used. The notebook also has an example preprocessing on the center combined dataset which is also copied in the pipeline. This notebook can be used alongside the feature engineering notebook but should represent the final pipeline for generating the datasets which will be fed into models. Ideas and preprocessing on separate datasets can be done at the end of the  notebook or instead of the center example.	This notebook contains the next preprocessing techniques so far:
            1. Logarthiming the target variable because it is right skewed to enforce normal distribution; 
            1. Dropping ozone and windGust variables; 
            1. Dropping all rows where Foggy is nan to drop correlated rows with missing temperature values; 
            1. Correlation analysis;
            1. Plots for outlier detection; 
            1. setting values of CO>300, NO2>250 and PM25>1000 to nans;
            1. Interpolating each missing col with limit=2 and default interpolation;
            1. Replacing windBearing with 0 if NaN;
            1. Imputing pressure such that if the row is NaN we replace it with the median value of that hour of that month for each year(same for precipProb,precipInt,medianUvi,windSpeed);
            1. Filling other nans of uvIndex with mean;
            1. Dropping CO2,CO,SO2,NO2 since 70% of values are missing;
            1. Dropping AQI to generate new one;
            1. Imputing O3 and PM25 the same way as before and imputing left over nans with limit=3;
            1. Generating AQI features for PM25,PM10,O3 by getting the mean for the last 1 day of the corresponding features(looked online);
            1. Generating lag feature for PM10 which is mean of the last 3 hours;
            1. Generating delta features(current-prev) for cols: 'O3', 'PM10', 'PM25', 'cloudCover', 'dewPoint', 'humidity', 'precipAccumulation', 'precipIntensity', 'precipProbability','pressure', 'temperature', 'uvIndex', 'visibility', 'windBearing','windSpeed','AQI_PM25', 'AQI_PM10', 'AQI_O3','PM10_history'
            1. Doing skew analysis on every numerical feature and then doing box cot transformation or log transformation on skewed features with skeweness>0.75
            this takes a very long time (~30mins)
    - The 'EDA and clustering' folder contains the 'EDA and clustering' notebook for exploratory data analysis of the combined datasets. In this notebook we do stationarity tests, generate the rolling mean and std and transform the time series for each pollutant into stationary series, removing seasonal trends etc. It contains various plots/visualizations and a segment dedicated for clustering, where the time series for each pollutant are mapped into the Fisher-Shannon plane and clustered with algorithms from the course, using the complexity-invariant distance metric.
    - The model evaluation folder contains the notebooks:
        - ModelEvaluationPipeline - main notebook of the folder. Used for using already optimized (hyperparametar wise) models to use as regressive models to predict the PM10 value for the next x hours. Only the PM10 values are shifted up in the dataset for x. In this way, the interval [-2x,-x] of the dataset if used as evaluation set, the model will learn the relationship how to predict the next x values(since the PM10 are shifted). The training set finally consists of the interval [0,-2x] and the final evaluation(test) set is [-2x,-x]. Each model's prediction is evaluated and the best one is chosen to generate the submission file in the sumbission folder. Refer to the Data description in the Data folder for more. 
        - XGBoost training notebook should be used to train and test new models on the combined preprocessed datasets. Contains grid search techniques for hyperparametar tuning.
        - \* This folder also contains the scores from our predictive models, organized into subfolders that contain:
            - The 'plots' subfolder contains a plot for each of the trained models in the models subfolder. The plot shows the predicted trend of the PM10 var vs the actual trend for the last X hours which the models are predicting.
            - The 'submissions' folder contains predictions only from the best model in the models subfolder in the format row:PM10_prediction.
            - The 'scores.csv' file contains the MAE(mean absolute error) from each model in the models subfolder.
- The 'Papers' folder contains all papers that we read and used as guidelines to our project.

- The 'Data collection scripts' folder contains scripts that we used to retrieve the data from the pulse.eco API.

