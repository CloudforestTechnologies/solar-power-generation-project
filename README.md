# Solar Panel Output Modelling

Introduction
---

This modelling/analysis project investigates the performance and behaviour of solar panels generating electricity for the Indian Power Network, using datasets from two generation plants made available on Kaggle.

Solar panel arrays have a high initial capital cost, repaid by generating stable quantities of electricity from the sun, and investment cases are predicated on being able to generate a certain amount of power to make the plant cost-effective. 

![Image of Solar Panels](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Miscellaneous/solar_panel_low_res_201110.jpg)

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

Steps where taken to consolidate the individual datasets for performance and sensor readings for each plant, using dates and times a common reference.

The datasets show a clear cyclic profile for the power generation profiles, so it should be possible to create an accurate model for predicting plant performance, given time of day and ambient conditions:

![Irradiation Time-Series for Plant 1](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Reports/Figures/WJ_Irradiation_Scatter_Plant1_2021_07_12-16_57_15.jpg)

Some data was found to be incorrect, whilst some time steps were missing associated data. In some cases, obviously erroneous data was set to zero (for example, power generation during hours of darkness), and in other cases missing values were filled in via interpolation.

To help with understanding the data, and to possibly support clustering techniques, features were engineered at an hourly level and added to the dataset.

Identifying Panels in Need of Cleaning or Maintenance
---

Machine learning models were initially developed to predict DC power generation for each plant (as DC Power, AC Power and electrical power output are all closely related). These models included regression models built with the sklearn module, and neural networks developed using Keras / Tensorflow.

The best-performing model for DC power generation was a 6-layer sequential neural network, which produced a RMSE of 1156 

Predicting Power Output
---



Installation & Setup
---

The following packages are used within this project:

numpy, pandas, matplotlib, seaborn, sklearn, keras.

Cloning
---

Clone this repository from: 

Acknowledgements
---

The kaggle project providing the data for this work can be accessed at: .