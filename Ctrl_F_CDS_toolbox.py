"""
This script defines a CDStoolbox application for visualizing temperature data and time series plots.
The link to access this is application: 
The application consists of the following components:
1. An outer application that displays a dynamic map of mean annual temperatures for selected years.
2. A dropdown input widget to select a year for which to display temperature data.
3. When the user clicks on the map, it launches a child application to display a time series plot of temperature data
   for the selected location and year.
4. The child application receives location information (latitude and longitude) from the map click event and monthly
   temperature data for the selected year.

Functions:
- `plot_time_series(location, monthly_temperature)`: Child function that plots a time series at the clicked location.
- `application(year)`: Main application function that retrieves temperature data for the selected year and displays a
  dynamic map of mean annual temperatures. It also launches the child application when the map is clicked.

"""

import cdstoolbox as ct

# Create a dictionary that contains the layout properties
app_layout = {
    'output_align': 'bottom'
}

# Initialise a child application
@ct.child()

# Add the livefigure of the child application as an output widget
@ct.output.livefigure()

# Define a child function plotting a time series at the clicked location
# The child app takes location and monthly temperature as inputs. Location is automatically passed by the "click on map" event in the main application
def plot_time_series(location, monthly_temperature):
    """
    This function generates a time series plot of temperature data for a specific location.

    Parameters:
    - location (dict): A dictionary containing the latitude and longitude of the selected location.
    - monthly_temperature (cdstoolbox.cube.Cube): Monthly temperature data for the selected year.

    Returns:
    - fig (cdstoolbox.chart.Figure): The time series plot as a CDStoolbox Figure object.
    """
    
    # Get lat, lon from the clicked location
    lat, lon = location['lat'], location['lon']
    
    # Extract data at the clicked location
    data_sel = ct.geo.extract_point(monthly_temperature, lon=lon, lat=lat)
    
    # Create a line plot of the selected time series
    fig = ct.chart.line(data_sel)

    return fig

# Initialise the application
@ct.application(
    title='Ctrl-F', 
    fullscreen=True,
    layout = app_layout
)

# Add an input widget that is a drop-down menu.
@ct.input.dropdown('year', values=[2020, 2021, 2022, 2023], label='Year')

# Define a livemap output launching the child app when the map is clicked
@ct.output.livemap(click_on_map=plot_time_series)

# Define an application function which returns a livemap showing the annual mean temperature
def application(year):  
    """
   This function serves as the main application and displays a dynamic map of mean annual temperatures for the selected year.
   It also launches a child application when the map is clicked to display a time series plot of temperature data.

   Parameters:
   - year (int): The selected year for which to display temperature data.

   Returns:
   - plot (cdstoolbox.livemap.Livemap): The dynamic map displaying mean annual temperatures as a CDStoolbox Livemap object.
   """
   
    # Retrieve full resolution monthly average temperature data for the selected year
    monthly_temperature_data = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels-monthly-means',
        {
            'product_type':'monthly_averaged_reanalysis',
            'variable':[
                '2m_temperature'
            ],
            'year': year,
            'month':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12'
            ],
            'time':'00:00',
            }
    )
    
    
     
    
    # Compute the mean annual temperature to plot as a heatmap
    mean_annual_temperature = ct.cube.average(monthly_temperature_data, dim='time')
    
    # Define arguments to pass to the child app
    child_kwargs_dict = {'monthly_temperature': monthly_temperature_data}
    
    
  
    
    # Plot mean annual temperature as a layer on a dynamic map
    plot = ct.livemap.plot(
        mean_annual_temperature,
        click_kwargs= child_kwargs_dict,
    )
    
    return plot

