"""Process river regions shapefiles provided by Bureau of Meteorology.

http://www.bom.gov.au/water/about/riverBasinAuxNav.shtml
provides links to download the regions but not in shapefile format,
so we reached out and obtained a shapefile version directly from the BoM

"""

import geopandas as gp

river_regions = gp.read_file('V32_RiverRegions.zip')
river_regions = river_regions.drop(columns=[
    'OBJECTID',
    'HydroID',
    'SrcFCName',
    'SrcFType',
    'SrcType',
    'SourceID',
    'FeatRel',
    'FSource',
    'AttrRel',
    'AttrSource',
    'PlanAcc',
    'Symbol',
    'TextNote',
    'AlbersArea',
    'Shape_Leng',
    'Shape_Area',
])
river_regions = river_regions[['RivRegName', 'RivRegNum', 'Division', 'geometry']]
river_regions.to_file('/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/river_regions/river_regions.shp')
