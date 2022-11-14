# Shapefiles

The repository contains information about the shapefile collection that forms part of the
Australian Community Reference Climate Data Collection @ NCI:

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/aus_states_territories/`
- Shapefiles describing the states and territories of Australia
- See `states_territories.ipynb` for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/australia/`
- Shapefiles describing the Australian coastline
- See `australia.ipynb` for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/broadacre_regions/`
- Shapefiles describing the Australian Bureau of Agricultural and Resource Economics and Sciences (ABARES) broadacre zones and regions
- See `broadacre_regions.ipynb` for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/nrm_regions/`
- Shapefiles describing the natural resource management (NRM) clusters
- See `nrm_regions.ipynb` for details

`/g/data/ia39/aus-ref-clim-data-nci/shapefiles/data/river_regions/`
- Shapefiles describing the topographic drainage divisions and river regions derived from the Australian Hydrological Geospatial Fabric
- See `river_regions.ipynb` for details


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
The [unseen](https://github.com/AusClimateService/unseen/blob/bd1dd32f0de81ff03bf862eee0f14715e3d5bfbe/unseen/spatial_selection.py#L97)
library has built on regionmask to provide more sophisticated functionality.

#### Other languages

TODO.
