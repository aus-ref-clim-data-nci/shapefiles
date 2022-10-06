## Shapefiles

The repository contains information about commonly used shapefiles for climate research in Australia.

#### Australia

The Australian Bureau of Statistics maintains the Australian Statistical Geography Standard (ASGS).
The latest release is [Edition 3](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3).

The original
[ABS shapefiles](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files) contain some shapes/geometries that can confuse some software packages
(e.g. 'other territories', 'outside australia'),
so the `australia.ipynb` and `aus_states_territories.ipynb` notebooks download the original shapefiles
and remove unneeded rows and columns.

See the `australia/` and `aus_states_territories/` directories in this repository for the new shapefiles
with unnecessary information removed.

#### Natural Resource Management (NRM) clusters

The Climate Change in Australia projections defined a set of natural resource management clusters.
The corresponding shapefiles can be downloaded [here](https://www.climatechangeinaustralia.gov.au/en/overview/methodology/nrm-regions/).
They are in a format that is typically useable without any manipulation.

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


