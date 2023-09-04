import cdstoolbox as ct

"""
This script is still under-development with bugs .

This script utilizes the CDStoolbox library to create a precipitation visualization application with polygon-based area selection.
In order to interact with this application, run this script on the CDS ToolBox Editor.

The application consists of the following components:
1. An outer application that displays a dynamic map of mean annual precipitation for selected year.
2. A dropdown input widget to select a year for which to display precipitation data.
3. When the user clicks on the map, it launches a child application to display a time series plot of precipitation data
   for the selected area and year.
4. The child application receives shape information from the map draw event and monthly
   precipitation data for the selected year.
   
Functions:
- `plot_time_series(params, monthly_precipitation)`: Generate a time series plot for a user-selected area.
- `application(year)`: Display mean annual precipitation and launch a child app for time series plots.

"""
# This code attempts to generate timeseries based on polygon area selection
# This code builds on Jevaughn's code for click based charts
# Create a dictionary that contains the layout properties
app_layout = {
    'output_align': 'bottom'
}

# Initialise a child application
@ct.child()

# Add the livefigure of the child application as an output widget
@ct.output.livefigure()

# Define a child function plotting a time series for the user-selected area
# The child app takes parameters generated from the user interaction and monthly precipitation as inputs. The parameters (containing the shape) are automatically passed by the "draw a shape" event in the main application

def plot_time_series(params, monthly_precipitation):
    """
    This function generates a time series plot for the user-selected area.

    Parameters:
    - params (dict): A dictionary containing user-generated shape coordinates.
    - monthly_precipitation (cdstoolbox.cube.Cube): Monthly precipitation data for the selected year.

    Returns:
    - fig (cdstoolbox.chart.Figure): The time series plot as a CDStoolbox Figure object.

    """
    # Introducing a try block to understand the origin of error
    try:
        # Get geometry from params
        coords_list = params['geometry']['coordinates'][0]
        print(coords_list)

        lons = [ a for a,b in coords_list ]
        lats = [ b for a,b in coords_list ]
        print(lons)
        
        # Generate CDS remote shape from the lats and lons lists of the vertices user selected area
        shape= ct.shapes.polygon(lons, lats)
        #shape2 = ct.shapes.get_geojson(shape)
        #print(shape2)
        print(shape)
        print(type(shape))
        print(len(shape))

        # Extract data in the AOI
        data_sel = ct.shapes.average(monthly_precipitation, shape)
   
    except(AttributeError,TypeError):
        print("error")
        
        # Create a line plot of the selected time series
    fig = ct.chart.line(data_sel)
    return fig


# Initialise the application
@ct.application(
    title='Ctrl F - Precipitation', 
    fullscreen=True,
    layout = app_layout
)
# Add an input widget that is a drop-down menu.
@ct.input.dropdown('year', values=[2020, 2021, 2022, 2023], label='Year')
# Define a livemap output launching the child app when the map is clicked
@ct.output.livemap(draw_a_shape=plot_time_series)

# Define an application function which returns a livemap showing the annual mean precipitation
def application(year):  
    
    """
    This function serves as the main application and displays a dynamic map of mean annual precipitation for the selected year.
    It also launches a child application when the map is clicked to display a time series plot of precipitation data.

    Parameters:
    - year (int): The selected year for which to display precipitation data.

    Returns:
    - plot (cdstoolbox.livemap.Livemap): The dynamic map displaying mean annual precipitation as a CDStoolbox Livemap object.

    """
    
    try:
        # Retrieve full resolution monthly average precipitation data for the selected year
        monthly_precipitation_data = ct.catalogue.retrieve(
            'reanalysis-era5-single-levels-monthly-means',
            {
                'product_type':'monthly_averaged_reanalysis',
                'variable':[
                    'total_precipitation'
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
        # Compute the mean annual precipitation to plot as a heatmap
        mean_annual_precipitation = ct.cube.average(monthly_precipitation_data, dim='time')

        # Define arguments to pass to the child app
        child_kwargs_dict = {'monthly_precipitation': monthly_precipitation_data}  

        # Plot mean annual precipitation as a layer on a dynamic map
        plot = ct.livemap.plot(
            mean_annual_precipitation,
             draw_kwargs= child_kwargs_dict,
        )
    except(AttributeError,TypeError):
        print("error")
        
    return plot