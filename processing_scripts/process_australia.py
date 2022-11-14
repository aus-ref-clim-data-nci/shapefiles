"""Process Australia shapefiles provided by the Australian Bureau of Statistics.

Removes some redundant columns and also the 'outside australia' row
because the corresponding geometry is empty and confuses some software packages.

"""

import geopandas as gp

gdf = gp.read_file('https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/AUS_2021_AUST_SHP_GDA2020.zip')

gdf = gdf.drop([1])
gdf = gdf.drop(columns=['CHG_FLAG21', 'CHG_LBL21'])

gdf.to_file('../shapefiles_australia/australia.shp')