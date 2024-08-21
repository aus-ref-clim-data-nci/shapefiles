"""Process Australia shapefiles provided by the Australian Climate Service.

Converts coordinates from northings/eastings to lat/lon coordinates.

Removes some redundant columns 

"""

import geopandas as gp

url = "https://services-ap1.arcgis.com/Xoz8Es66HpfM8jP9/arcgis/rest/services/NCRA_Marine_Region_with_metadata/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

gdf = gp.read_file(url).to_crs("EPSG:4326")

gdf = gdf.drop(columns=["FID", "Shape__Area", "Shape__Length"])
gdf = gdf.rename(columns = {"Region_name":"RegionName"})

gdf.to_file('/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/NCRA_Marine_region/NCRA_Marine_region.shp')
