# Shapefiles

The Australian Community Reference Climate Data Collection @ NCI shapefile collection
contains the following:

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/aus_local_gov/`
- Shapefiles describing the local government areas of Australia
- See [`aus_local_gov.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/aus_local_gov.ipynb) for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/aus_states_territories/`
- Shapefiles describing the states and territories of Australia
- See [`aus_states_territories.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/aus_states_territories.ipynb) for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/australia/`
- Shapefiles describing the Australian coastline
- See [`australia.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/australia.ipynb) for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/broadacre_regions/`
- Shapefiles describing the Australian Bureau of Agricultural and Resource Economics and Sciences (ABARES) broadacre zones and regions
- See [`broadacre_regions.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/broadacre_regions.ipynb) for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/NCRA_Marine_region/`
- Shapefiles describing the National Climate Risk Assessment (NCRA) marine region for Australia.
- See [`ncra_marine_region.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/ncra_marine_region.ipynb) for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/ncra_regions/`
- Shapefiles describing the National Climate Risk Assessment (NCRA) regions of Australia.
- See [`ncra_regions.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/ncra_regions.ipynb) for details
  
`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/NCRA_regions_coastal_waters_GDA94/`
- Shapefiles describing the Australian coastal waters areas divided by NCRA regions
- See [`ncra_coastal_waters.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/ncra_coastal_waters.ipynb) for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/nrm_regions/`
- Shapefiles describing the natural resource management (NRM) clusters
- See [`nrm_regions.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/nrm_regions.ipynb) for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/river_regions/`
- Shapefiles describing the topographic drainage divisions and river regions derived from the Australian Hydrological Geospatial Fabric
- See [`river_regions.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/river_regions.ipynb) for details


## Software

Most programming languages have libraries for reading in shapefiles
and selecting geographic data points that fall within them. 

#### Python

If your workflow is based around Python and xarray,
you can typically read a shapefile using [geopandas](https://geopandas.org).
The resulting GeoDataFrame can then be passed to a function from the
[regionmask](https://regionmask.readthedocs.io) or
[clisops](https://clisops.readthedocs.io) library
to select grid points from an xarray data set that fall within the shape/s.

See [`python_tutorial.ipynb`](https://github.com/aus-ref-clim-data-nci/shapefiles/blob/master/python_tutorial.ipynb)
for a worked example using regionmask and the shapefiles in this collection.

#### Other languages

TODO.
