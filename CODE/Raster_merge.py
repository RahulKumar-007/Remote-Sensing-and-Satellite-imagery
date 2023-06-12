from osgeo import gdal

def merge_raster_files(input_files, output_file):
    # Open the first input raster to get the spatial and projection information
    dataset = gdal.Open(input_files[0], gdal.GA_ReadOnly)
    driver = gdal.GetDriverByName('GTiff')

    # Get the spatial and projection information from the first input raster
    geotransform = dataset.GetGeoTransform()
    projection = dataset.GetProjection()

    # Create an output raster with the same size, resolution, and projection as the first input raster
    output_dataset = driver.Create(output_file, dataset.RasterXSize, dataset.RasterYSize, len(input_files),
                                   dataset.GetRasterBand(1).DataType)

    output_dataset.SetGeoTransform(geotransform)
    output_dataset.SetProjection(projection)

    # Loop through each input raster and copy its bands to the output raster
    for i, input_file in enumerate(input_files):
        input_dataset = gdal.Open(input_file, gdal.GA_ReadOnly)
        for band_index in range(input_dataset.RasterCount):
            band = input_dataset.GetRasterBand(band_index + 1)
            output_band = output_dataset.GetRasterBand(i + 1)
            output_band.WriteArray(band.ReadAsArray())
            output_band.FlushCache()

    # Close the datasets
    output_dataset = None
    dataset = None

# Example usage
input_files = ['input1.tif', 'input2.tif', 'input3.tif']
output_file = 'output.tif'
merge_raster_files(input_files, output_file)
