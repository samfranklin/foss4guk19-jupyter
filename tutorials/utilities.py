import rasterio as rs
from matplotlib import pyplot
from rasterio.plot import show
from rasterio.plot import show_hist
import fiona
from shapely.geometry import shape, mapping
from fiona.crs import from_epsg

def make_nice_single_raster_plot(input_raster,no_of_histg_bins):
    fig, (ax1, ax2, ax3) = pyplot.subplots(1,3, figsize=(21,7))
    show(input_raster.read(), ax=ax1, transform=input_raster.transform, cmap='BrBG', title='#NoRainbow')
    show(input_raster.read(), ax=ax2, transform=input_raster.transform, contour=True, title='contours')
    show_hist(input_raster, bins=no_of_histg_bins, lw=0.0, stacked=False,histtype='stepfilled', title="Histogram of height vals")


def make_equidistant_points_from_linstring(line_data,interval,crs,output_path):

    try:
        # open the line shapefile
        line = fiona.open(line_data)

        # example with the first feature
        firstline = next(iter(line))

        # transform to shapely geometry
        first = shape(firstline['geometry'])

        # length of the LineString
        length = first.length

        # creation of the resulting shapefile
        schema = {'geometry': 'Point','properties': {'id': 'int'},}
        
        with fiona.open(output_path, mode='w', crs=from_epsg(crs), driver='GeoJSON', schema=schema)  as output:
            
            # create points along the line
            for distance in range(0,int(length),interval):
                point = first.interpolate(distance)   
                output.write({'geometry':mapping(point),'properties': {'id':1}})
    except e as Exception:
        print(e)
		