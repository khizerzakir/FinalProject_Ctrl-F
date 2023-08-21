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
# The child app takes location and monthly precipitation as inputs. Location is automatically passed by the "click on map" event in the main application
def plot_time_series(location, monthly_precipitation):
    
    # Get lat, lon from the clicked location
    lat, lon = location['lat'], location['lon']
    
    # Extract data at the clicked location
    data_sel = ct.geo.extract_point(monthly_precipitation, lon=lon, lat=lat)
    
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
@ct.output.livemap(click_on_map=plot_time_series)

# Define an application function which returns a livemap showing the annual mean precipitation
def application(year):  
    
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
        click_kwargs= child_kwargs_dict,
    )
    
    return plot

