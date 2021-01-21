# Solar Panel Output Modelling

Introduction
---

This data analytics and predictive modelling project investigates the performance and behaviour of solar panels generating electricity for the Indian Power Network, using datasets from two generation plants made available on Kaggle.

The project starts with an exploration of the datasets, followed by the development of models for predicting plant performance, and solutions for detecting panels in need of maintenance using regression and neural network frameworks (Keras API). 

![Image of Solar Panels](https://github.com/PMetcalf/solar-power-generation-project/blob/master/Miscellaneous/solar_panel_low_res_201110.jpg)

Data has been gathered at two Indian solar power plants over a 34 day period. There are two datasets for each plant: One for power generation, and one for environmental sensor readings. 

The power generation datasets are gathered at the inverter level, and each inverter has multiple lines of solar panels attached to it. The sensor data is gathered at plant level, with a single array of optimally-placed sensors.

This project attempts to provide solutions for power station operation: Can we predict power generation over the next couple of days? Can we identify the need for panel cleaning or maintenance? Can we identify faulty or suboptimally performing equipment? 

Project Objectives
---

1. Develop predictive models for solar power generation based on historic data.
2. Develop predictive models that can identify solar panels that are faulty or in need of maintenance.

Exploring the Dataset
---

Jupyter notebooks were used to conduct exploratory analysis on the dataset, first checking for missing values and incorrect datatypes, and then investigating relationships between parameters.

Steps where taken to consolidate the individual datasets for performance and sensor readings for each plant, using dates and times a common reference.

The datasets show a clear cyclic for the power generation profiles, so it should be possible to create an accurate model for predicting plant performance, given time of day and ambient conditions:

[Insert image of plant data distribution]

There are strong linear relationships between generated power and irradiation (as would be expected), and a slight inverse relationship between ambient temperature and power generation:

[Insert image of correlation matrix]

Whilst there was some individual variance between cell performance, it should be possible to develop models to identify abnormal cell performance.

Predictive Modelling
---

Machine learning models were initially developed to predict DC power generation for each plant (as DC Power, AC Power and electrical power output are all closely related). These models included regression models built with the sklearn module, and neural networks developed using Keras / Tensorflow.

The best-performing model for DC power generation was a 6-layer sequential neural network, which produced a RMSE of 1156 

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