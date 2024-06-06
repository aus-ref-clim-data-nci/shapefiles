"""Process states and territories shapefiles provided by the Australian Bureau of Statistics.

Removes some redundant columns and also the 'outside australia' row
because the corresponding geometry is empty and confuses some software packages.

"""

import geopandas as gp

gdf = gp.read_file('https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/STE_2021_AUST_SHP_GDA2020.zip')

gdf = gdf.drop([9])
gdf['ABBREV'] = ['NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT', 'OT']
gdf = gdf[['STE_NAME21', 'ABBREV', 'AREASQKM21', 'LOCI_URI21', 'geometry']]

gdf.to_file('/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/aus_states_territories/aus_states_territories.shp')
