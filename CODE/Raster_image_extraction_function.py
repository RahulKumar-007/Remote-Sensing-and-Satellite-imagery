import rasterio
from rasterio.mask import mask
import geopandas as gpd
import numpy as np

def extract_raster_with_shapefile(raster_path, shapefile_path, output_path):
    # Open the raster file
    src = rasterio.open(raster_path)

    # Open the shapefile
    shapefile = gpd.read_file(shapefile_path)

    # Make sure the shapefile and raster have the same coordinate reference system (CRS)
    shapefile = shapefile.to_crs(src.crs)

    # Extract the geometries from the shapefile
    geometries = shapefile.geometry.values

    # Extract the raster image using the shapefile geometries
    out_image, out_transform = mask(src, geometries, crop=True)

    # Convert the output image to uint8
    out_image = out_image.astype(np.uint8)

    # Create a new raster file with the extracted image
    out_meta = src.meta.copy()
    out_meta.update(dict(height=out_image.shape[1], width=out_image.shape[2], transform=out_transform, dtype='uint8'))

    with rasterio.open(output_path, 'w', **out_meta) as dst:
        dst.write(out_image)
