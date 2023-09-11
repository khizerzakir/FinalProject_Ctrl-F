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

1. .yml file
2. .txt file

There are 2 notebooks presented in the repo. The first notebook (LINK) showcases how to access the CDS using the CDS API to acquire temperature data for a defined date range (more explanation in the script).

Following the data access aspect, the next steps involved reading the documentation on Xarray and other important libraries to better understand NetCDF files. The second notebook (LINK) explores the data analysis conducted on the files from the CDS, particularly, visualising the temperature data. Included in the second notebook, the xcube library is explored for producing a local plot viewer. This aspect is still under development.

## The CDS Toolbox

1. **Precipitation for a selected country**
   



Application 1:
Select a month and year and then select a European country. The selection then returns a time series of the monthly average precipitation.

Application 1 Demo:
https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/9694809b-312e-44d6-b9fb-df0bec68df07




Application 2: 
Select the year to display the mean precipitation and then draw the desired area to produce a time series. This tool has some errors and does not display the time series. In future works, we aim to complete this application and get it fully operational.

Application 2 Demo:
https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/24e77f0c-4ed8-4085-8f74-e213752fefe6

Application 3:
Temperature

Application 3 Demo:
https://github.com/khizerzakir/FinalProject_Ctrl-F/assets/127128607/4dfaa075-129c-4558-a3d8-6bd16a5cf428








Temperature

## 
