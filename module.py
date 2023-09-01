import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import earthpy as et
import xarray as xr
import regionmask

# Plotting options
sns.set(font_scale=1.3)
sns.set_style("white")

# Optional - set your working directory if you wish to use the data
# accessed lower down in this notebook (the USA state boundary data)
os.chdir(os.path.join(et.io.HOME, 'data'))

# Function to open the NetCDF file and return the xarray object
def open_netCDF_file(file_path):
    """
    Open a NetCDF file and return an xarray dataset.
    
    Parameters:
    file_path (str): Path to the NetCDF file.
    
    Returns:
    xarray.Dataset: The xarray dataset.
    """
    with xr.open_dataset(file_path) as file_nc:
        return file_nc

# Function to read the shapefile and return a GeoDataFrame
def read_shapefile(shp_path):
    """
    Read a shapefile and return a GeoDataFrame.
    
    Parameters:
    shp_path (str): Path to the shapefile.
    
    Returns:
    geopandas.GeoDataFrame: The GeoDataFrame.
    """
    return gpd.read_file(shp_path)

# Function to select an area of interest (AOI)
def select_area_of_interest(gdf, lat_min, lat_max, lon_min, lon_max):
    """
    Select an area of interest (AOI) from a GeoDataFrame.
    
    Parameters:
    gdf (geopandas.GeoDataFrame): The GeoDataFrame containing geometries.
    lat_min (float): Minimum latitude of the AOI.
    lat_max (float): Maximum latitude of the AOI.
    lon_min (float): Minimum longitude of the AOI.
    lon_max (float): Maximum longitude of the AOI.
    
    Returns:
    geopandas.GeoDataFrame: The selected AOI as a GeoDataFrame.
    """
    return gdf.cx[lon_min:lon_max, lat_min:lat_max]

# Function to slice the data by time and spatial extent
def slice_data(data, start_date, end_date, lon_slice, lat_slice):
    """
    Slice the data by time and spatial extent.
    
    Parameters:
    data (xarray.Dataset): The xarray dataset containing the data.
    start_date (str): Start date for the time slice (YYYY-MM-DD).
    end_date (str): End date for the time slice (YYYY-MM-DD).
    lon_slice (slice): Longitude slice (e.g., slice(0, 10)).
    lat_slice (slice): Latitude slice (e.g., slice(40, 50)).
    
    Returns:
    xarray.Dataset: The sliced dataset.
    """
    return data.sel(
        time=slice(start_date, end_date),
        longitude=lon_slice,
        latitude=lat_slice
    )

# Function to plot a GeoDataFrame
def plot_geodataframe(gdf, title=""):
    """
    Plot a GeoDataFrame.
    
    Parameters:
    gdf (geopandas.GeoDataFrame): The GeoDataFrame to be plotted.
    title (str): Title for the plot.
    """
    f, ax = plt.subplots()
    gdf.plot(ax=ax)
    ax.set(title=title)
    plt.show()

# Function to mask data based on a regionmask
def mask_data_with_regionmask(data, region_mask):
    """
    Mask data based on a regionmask.
    
    Parameters:
    data (xarray.Dataset): The xarray dataset containing the data.
    region_mask (regionmask.Regions): The region mask to be used for masking.
    
    Returns:
    xarray.Dataset: The masked dataset.
    """
    return data.where(region_mask)

# Function to plot time series data
def plot_time_series(data, col_name, title=""):
    """
    Plot time series data.
    
    Parameters:
    data (xarray.Dataset): The xarray dataset containing the data.
    col_name (str): Name of the data variable to plot.
    title (str): Title for the plot.
    """
    data[col_name].plot(col='time', col_wrap=1)
    plt.title(title)
    plt.show()


