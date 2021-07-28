# Solar Panel Output Modelling

Introduction
---

This modelling/analysis project investigates the performance and behaviour of solar panels generating electricity for the Indian Power Network, using datasets from two generation plants made available on Kaggle.

Solar panel arrays have a high initial capital cost, repaid by generating stable quantities of electricity from the sun, and investment cases are predicated on being able to generate a certain amount of power to make the plant cost-effective. 

![Solar Panels](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Miscellaneous/solar_panel_low_res_201110.jpg)

The project starts with an exploration of the datasets and feature engineering, followed by the development of models for predicting plant performance, and solutions for detecting panels in need of maintenance using regression and neural network frameworks (Keras API). 

Data has been gathered at two Indian solar power plants over a 34 day period. There are two datasets for each plant: One for power generation, and one for environmental sensor readings (temperatures, irradiation). 

The power generation datasets are gathered at the inverter level, and each inverter has multiple lines of solar panels attached to it. The sensor data is gathered at plant level, with a single array of optimally-placed sensors.

This project attempts to provide solutions for power station operation: Can we predict power generation over the next couple of days? Can we identify the need for panel cleaning or maintenance? Can we identify faulty or suboptimally performing equipment? 

Project Objectives
---

1. Develop solutions for identifying panels that are faulty or may need maintenance.
2. Develop solutions for identifying when panels may collectively be in need of cleaning.
3. Develop solutions that can predict solar panel output from current conditions (and potentially forecast future output).

Exploring the Dataset
---

Jupyter notebooks were used to conduct exploratory analysis on the dataset, first checking for missing values and incorrect datatypes, and then investigating relationships between parameters.

Steps where taken to consolidate the individual datasets for performance and sensor readings for each plant, using dates and times as a common data reference.

The datasets show a clear cyclic profile for the power generation profiles, so it should be possible to create an accurate model for predicting plant performance, given time of day and ambient conditions:

![Irradiation Time-Series for Plant 1](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Reports/Figures/WJ_Irradiation_Scatter_Plant1_2021_07_12-16_57_15.png)

Some data was found to be incorrect, whilst some time steps were missing expected datapoints. In some cases, obviously erroneous data was set to zero (for example, power generation during hours of darkness), and in other cases missing values were generated via interpolation.

To help with understanding the data, and to possibly support clustering techniques, summary features were engineered at a daily and hourly level, and added to the dataset.

Identifying Panels in Need of Cleaning or Maintenance
---

How can faulty panels be identified, or those in need of maintenance?

Assumptions on the operational behaviour and failure characteristics of solar panels enabled identification strategies to be developed.

A good inverter should be consistently productive, so features related to consistency and productivity can create insights into failing panels. Panels with large numbers of zero outputs compared to peers could well be in need of a maintenance intervention:

![Plant 1 Daily Yield - Zero Output](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Reports/Figures/WJ_Plant1_Avg_Daily_Yield_Zero_Output_2021_07_14-10_48_21.png)

When many panels are collectively producing less power output than predicted for a given level of irradiation, it may be that the panels need cleaning. A simple linear regression model can be trained to forecast output for a given set of conditions, and the number of 'sub-prediction' real values can be measured:

![Plant 1 Forecast v. Actual Output](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Reports/Figures/WJ_Plant1_Avg_DC_Power_Prediction_2021_07_14-10_49_17.png)

This effect seems to be born out in the datasets, where mean output gradually drops versus predicted output and then seemingly recovers, possibly as a result of a cleaning operation.

Predicting Power Output
---

Predicting expected generation for a given set of conditions can be useful for grid management, fault detection and cleaning, and so the project included developing predictive models using a couple of different techniques.

In an expanded scenario, historical and projected weather data would be available and would enable the use of models to forward-project power output ahead of time. In the absence of this data, modelling is largely limited to making predictions based on current conditions. 

Machine learning models were initially developed to predict DC power generation for each plant (as DC Power, AC Power and electrical power output are all closely related). These models included regression models built with the sklearn module, and neural networks developed using Keras / Tensorflow.

Linear regression models developed a tendency to underpredict data at higher power outputs, probably as a result of faulty (underperforming) panels being present in the training data:

![Plant 1 Linear Regression Prediction Error](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Reports/Figures/WJ_LinReg_Plant1_Error_Plot_2021_06_08-10_10_47.png)

Interestingly, regression models trained using neural networks trained on the same datasets seemed to avoid this effect, although RMSE/MAE performance was comparable to similar linear regression models (prediction errors were spread more evenly between over and under prediction):

![Plant 1 NN Prediction Error](https://github.com/PMetcalf/solar-power-generation-project/tree/master/Reports/Figures/WJ_MLP_Opt_Pt1_Prediction_Error_2021_07_14-11_18_29.png)

Overall, the models are flawed as absolute predictors, but useful indicators. 

Installation & Setup
---

The following packages are used within this project:

numpy, pandas, matplotlib, seaborn, sklearn, keras.

Cloning
---

Clone this repository from: https://github.com/PMetcalf/solar-power-generation-project.git

Acknowledgements
---

The kaggle project providing the data for this work can be accessed from https://www.kaggle.com/anikannal/solar-power-generation-data.