mport rasterio
from rasterio.mask import mask
import geopandas as gpd

# Open the raster file
raster_path = r'C:\Users\91639\Desktop\mergedmap.tif'
src = rasterio.open(raster_path)

# Open the shapefile
shapefile_path = r'C:\Users\91639\Desktop\punjab\Punjab.shp'
shapefile = gpd.read_file(shapefile_path)

# Make sure the shapefile and raster have the same coordinate reference system (CRS)
shapefile = shapefile.to_crs(src.crs)

# Extract the geometries from the shapefile
geometries = shapefile.geometry.values

# Extract the raster image using the shapefile geometries
out_image, out_transform = mask(src, geometries, crop=True)

# Create a new raster file with the extracted image
out_meta = src.meta.copy()
out_meta.update({
    'height': out_image.shape[1],
    'width': out_image.shape[2],
    'transform': out_transform
})

output_path = r'C:\Users\91639\Desktop\maskedPython.tif'
with rasterio.open(output_path, 'w', **out_meta) as dst:
    dst.write(out_image)
