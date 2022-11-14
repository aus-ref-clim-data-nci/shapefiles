"""Process local government area shapefiles provided by the Australian Bureau of Statistics.

Removes some redundant columns and also empty geometries.

"""

import geopandas as gp

gdf = gp.read_file('https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/LGA_2022_AUST_GDA2020_SHP.zip')

gdf = gdf[gdf['AREASQKM'] != 0.0]
gdf = gdf.drop(columns=['AUS_CODE21', 'AUS_NAME21'])

gdf.to_file('/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/aus_local_gov/aus_local_gov.shp')