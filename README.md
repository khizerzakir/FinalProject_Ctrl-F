# **Software Development Final Project**
# CTRL-F
**Group 5**

<p align="center">
<img src="ctrl+f.png" width="500"/>
</p>

# Overview

Climate change is the defining challenge of our time. Its impacts know no borders and all members of society are being affected. To tackle this challenge, there is a constant need for the development of sustainable solutions. One impact of rising temperatures and changing precipitation patterns is the occurrence of more large-scale wildfires. These wildfires damage/destroy ecosystems and pose significant health risks to human beings. The risk of fire is increased by warm and dry weather. This calls for continuous monitoring and dissemination of atmospheric and weather indicators that can help track and study wildfire conditions over different regions. We propose the development of a climate-related application; 'Ctrl+F (Fire)' that allows users to visualize atmospheric variables relevant for tracking wildfires, temperature, and precipitation at a desired location.

We set out to create a unified application with a graphical user interface to allow users to interact with the precipitation and temperature datasets disseminated by the Copernicus Climate Data Store (CDS). The objective included that the user should be able to explore the variables for a desired point location or any arbitrary area of interest (user-drawn shape). We were able to achieve the objective partially. The following section outlines the outputs generated in the process of fulfilling this objective.

# **Outputs**

In this project, we explored different ways of using CDS data repositories. As part of the exploration, we have generated the following scripts to process the CDS data:

**Jupyter Notebook:**
  1. Temperature time series
  2. Temperature masked for a selected area of interest

**CDS Toolbox Applications Developed:**
  1. Precipitation for a selected country
  2. Precipitation for a selected area of interest
  3. Temperature at a selected point location

## The Jupyter Notebook

The Python Environment and Requirements are outlined in the following files:

1. .yml file - [ctrl_f.yml](https://github.com/khizerzakir/FinalProject_Ctrl-F/blob/200fd76f78676bbfd23fe95d013ee1a7b8d217fc/ctrl_f.yml)
2. .txt file - [ctrl_f.txt](https://github.com/khizerzakir/FinalProject_Ctrl-F/blob/200fd76f78676bbfd23fe95d013ee1a7b8d217fc/ctrl_f.txt) 

There are 2 notebooks presented in the repo. The [first notebook](https://github.com/khizerzakir/FinalProject_Ctrl-F/blob/200fd76f78676bbfd23fe95d013ee1a7b8d217fc/temp2m_download.py) showcases how to access the CDS using the CDS API to acquire temperature data for a defined date range and area extent (more explanation in the script).

Following the data access aspect, the next steps involved reading the documentation on Xarray, geopandas, matlplotlib, regionmask and other essential libraries to better understand NetCDF files and extract the data for a specific shapefile/AOI. The [second notebook][(https://github.com/khizerzakir/FinalProject_Ctrl-F/blob/d77fde494ce96682e7db5b4e961ac17001833d85/Ctrl_F_Temperature_clipped_mask.ipynb)] explores the data analysis conducted on the file(s) from the CDS, particularly, visualising the temperature data. 
# Second Notebook Overview 
# Exploring Temperature Data in Portugal using OOP and Geospatial Analysis
**Dataset Information:**
- Dataset Title: ERA5-Land hourly data from 1950 to present
- Data Source: Copernicus Climate Change Service (C3S) Climate Data Store (CDS)
- DOI: [10.24381/cds.e2161bac](https://doi.org/10.24381/cds.e2161bac)
- Citation: Muñoz Sabater, J. (2019): ERA5-Land hourly data from 1950 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). DOI: 10.24381/cds.e2161bac (Accessed on DD-MMM-YYYY)

## Overview

This notebook explores temperature data for Portugal using an Object-Oriented Programming (OOP) approach and geospatial analysis techniques. The temperature data is sourced from the CDS datastore and is specifically downloaded for parts of the Iberian Peninsula. However, for this use case, we focus on extracting temperature data for Portugal for a single year. This notebook showcases how to read and visualize NetCDF (nc) files, as well as work with administrative boundaries of Portugal using GeoDataFrames.

The notebook is structured as follows:

### 1. Importing Required Libraries

We begin by importing essential Python libraries for data analysis, visualization, and geospatial analysis. This includes libraries such as `os`, `numpy`, `pandas`, `matplotlib`, `cartopy`, `seaborn`, `geopandas`, `earthpy`, `xarray`, and `regionmask`.

### 2. The `Temp` Class

In this section, we define the `Temp` class, which is designed to handle temperature-related data processing. The class includes methods for reading NetCDF files, reading shapefiles, filtering GeoDataFrames, extracting total bounds, and retrieving the CRS. The OOP approach helps organize and manage temperature-related data operations efficiently.

### Further Analysis

In the following section(s), we use the `Temp` class to read the NetCDF file containing temperature data and load the shapefile representing administrative boundaries. We filter the administrative boundaries to select only Portugal for further analysis. Later, We explore the temperature data by plotting it for a specific date range and spatial extent within Portugal. The visualization helps us understand the variation in temperature over time. Next part demonstrates how to work with GeoDataFrames to visualize administrative boundaries. We create a region mask for Portugal and visualize the respective temperature value for the region month wise. 

---
This notebook serves as a comprehensive guide to working with temperature data, administrative boundaries, and geospatial analysis techniques using an OOP approach. Feel free to adapt and extend the code for your specific research or analysis needs.

## The CDS Toolbox

1. **Precipitation for a selected country**
   
![Precip_1](https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/cd06cf5e-ec15-4f55-83ef-e203ddd90330)
_Figure 1: Precipitation map display based on time selection_

![Precip_2](https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/15474cdf-27af-4b3a-b337-b6ea10589af5)
_Figure 2: Time series created of monthly mean precipitation for a selected country (in this example, Spain 2022)_

A demonstration video can be found at the following link:
https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/9694809b-312e-44d6-b9fb-df0bec68df07 
  
**How it works:**

The user can select the month and year of interest from the drop-down. After selection, the map will display the average precipitation for the month selected. By default, December 2022 will be selected on the dropdown and the corresponding data displayed on the map. The next feature allows the user to select a country in Europe (the map should zoom to that country after selection) to generate a time series plot below the map. The time series displays the average monthly precipitation for the selected country.

The application script (python file: LINK) defines two main methods: one to display the map, and the other to display the time series plot. The method to display the map receives user input of month and year from the dropdown. Then, the user-selected country is passed from the map to the method that plots the precipitation time series.

2. **Precipitation for a selected area of interest**

![Screenshot 2023-09-08 075351](https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/c581aab1-b438-48cc-875d-86663e5380ac)
_Figure 3: Map display and selection of an area of interest_

![Screenshot 2023-09-08 075516](https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/ffb4ec6a-65ee-4fda-a868-b8c389625aa4)
_Figure 4: Time series plot for the selected area underdevelopment_

A demonstration video can be found at the following link:
https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/24e77f0c-4ed8-4085-8f74-e213752fefe6

**How it works:**

The user can select the year of interest from the drop-down. After selection, the map will display the annual precipitation average. By default, the year 2020 will be selected on the dropdown and the corresponding data displayed on the map. Then, click on the draw shape button ( ![](RackMultipart20230911-1-y0g9ku_html_47d10c6d35e29066.png) ) and draw an area of interest. Once the area is drawn, a time series plot is supposed to be generated below the map, displaying the monthly precipitation average in the selected area. However, currently, the plotting function is running into an error and is under active development.

The application script (python file: LINK) defines two main methods: one to display the map, and the other to display the time series plot. The method to display the map receives user input of year from the dropdown. Then, once the user interacts with the map, the shape information is passed from the map to the method that plots the precipitation time series.

3. **Temperature at a selected point location**
   
![Temperature shot 1](https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/4a2e2440-0ef8-4d92-8150-409f234f68b9)
_Figure 5: Annual average temperature displayed on the map for the selected year_

![Temperature shot 2](https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/d9387196-9951-4bba-ab10-d12a8b422630)
_Figure 6: Time series of temperature at the selected point_

A demonstration video can be found at the following link:
https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/24e77f0c-4ed8-4085-8f74-e213752fefe6

**How it works:**

The user can select the year of interest from the drop-down list ranging from 2020 to 2023. After selection, the map will display the average temperature for the year selected. By default, data is displayed for 2020. The next feature allows the user to select a point of interest to generate a time series plot below the map. The time series displays the average monthly temperature for the selected point for the selected year.

The application script (python file: LINK) defines two main methods: one to display the map, and the other to display the time series plot. The method to display the map receives user input of the year from the dropdown. Then, the user-selected point is passed from the map to the method that plots the temperature time series.

# Challenges

1. While developing the application of displaying a time series plot for a user-defined shape, a major challenge was in understanding the error message and finding out where exactly in the script the error was thrown and how to solve it. More documentation, including examples, on the [CDS toolbox shape objects](https://cds.climate.copernicus.eu/toolbox/doc/api.html#shapes) – regarding their construction and usage in cube sub-setting and aggregating methods would have been helpful. We could not find related issues on the [user forum](https://confluence.ecmwf.int/display/CUSF/C3S+Climate+Data+Store+Toolbox+User+Forum) either.

# Next Steps

1. In this project, we were able to achieve the objective of allowing users to interact with weather data on precipitation and temperature for desired locations. However, as a next step, we would like to build a unified application for interacting with both datasets. Further, we would like to spend more time fixing the error that we are currently facing in the application for displaying a time series plot for a user-defined shape. To do this, we also would like to engage with the [CDS Toolbox user community](https://confluence.ecmwf.int/display/CUSF/C3S+Climate+Data+Store+Toolbox+User+Forum) online and seek help. We then aim to integrate the draw-shape functionality into the main application.
2. We also explored the data through a Jupyter Notebook that informed the data processing in the application development. Going forward, we would also like to build the Jupyter Notebook further and use the xcube Python library to slice and dice the data from the C3S. Leveraging xcube's capabilities, we aim to build a dashboard interface for interacting with the data directly within the Notebook.





