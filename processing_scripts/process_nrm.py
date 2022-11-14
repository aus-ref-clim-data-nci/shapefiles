"""Process NRM regions shapefiles provided by Bureau of Meteorology.

The only difference with the shapefiles at
https://www.climatechangeinaustralia.gov.au/en/overview/methodology/nrm-regions/
is that the BoM files are clipped to the land boundary of Australia.

"""

import geopandas as gp

nrm_regions_file = 'NRM_regions_clipped_toAWRA/NRM_regions_clipped_toAWRA.shp'
nrm_regions = gp.read_file(nrm_regions_file)
nrm_regions = nrm_regions[0:15]

columns_to_drop = ['OBJECTID_1', 'OBJECTID', 'name', 'Shape_Leng', 'Shape_Area']
nrm_regions = nrm_regions.drop(columns=columns_to_drop)

columns_to_rename = {
    'label': 'SubClusNm',
    'code': 'SubClusAb',
    'C_code': 'ClusterAb',
    'C_Label': 'ClusterNm'
}
nrm_regions = nrm_regions.rename(columns=columns_to_rename)

nrm_regions['SupClusNm'] = [
    'Northern Australia',
    'Rangelands',
    'Northern Australia',
    'Northern Australia',
    'Eastern Australia',
    'Eastern Australia',
    'Southern Australia',
    'Southern Australia',
    'Southern Australia',
    'Southern Australia',
    'Southern Australia',
    'Southern Australia',
    'Southern Australia',
    'Eastern Australia',
    'Rangelands',
]
nrm_regions['SupClusAb'] = [
    'NA',
    'R',
    'NA',
    'NA',
    'EA',
    'EA',
    'SA',
    'SA',
    'SA',
    'SA',
    'SA',
    'SA',
    'SA',
    'EA',
    'R',
]
nrm_regions = nrm_regions[[
    'SubClusNm',
    'SubClusAb',
    'ClusterNm',
    'ClusterAb',
    'SupClusNm',
    'SupClusAb',
    'geometry',
]]

nrm_regions.to_file('../shapefiles_nrm_regions/nrm_regions.shp')