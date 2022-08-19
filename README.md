## Shapefiles

The repository contains commonly used shapefiles that require some manipulation before they can be easily used
with the [regionmask](https://regionmask.readthedocs.io) library.

### Australia

The Australian Bureau of Statistics maintains the Australian Statistical Geography Standard (ASGS).
The latest release is [Edition 3](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3).

In order to create regionmask-compatible shapefiles for Australia and individual states and territories,
I ran two notebooks (`australia.ipynb` and `aus_states.ipynb`) that download the original
[ABS shapefiles](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)
and remove unneeded rows and columns.

See the `australia/` and `aus_states_territories/` directories in this repository for the new regionmask-compatible shapefiles.

### Natural Resource Management (NRM) clusters

The Climate Change in Australia projections defined a set of natural resource management clusters.
The corresponding shapefiles can be downloaded [here](https://www.climatechangeinaustralia.gov.au/en/overview/methodology/nrm-regions/).
They are in a format that is useable without any manipulation.
