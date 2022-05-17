## Shapefiles

This repo contains information about the various shapefiles stored at `/g/data/xv83/dbi599/shapefiles/`.

## Australia

The Australian Bureau of Statistics maintains the Australian Statistical Geography Standard (ASGS). The latest release is [Edition 3](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3).

In order to create a shapefile for Australia and another for the states and territories,
I downloaded the relevant files [here](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files).
The notebooks in this directory (`australia.ipynb` and `aus_states.ipynb`) further manipulate those shapefiles
to remove unneeded rows and columns.

## Natural Resource Management (NRM) clusters

The Climate Change in Australia projections defined a set of natural resource management clusters.
The corresponding shapefiles can be downloaded [here](https://www.climatechangeinaustralia.gov.au/en/overview/methodology/nrm-regions/).
They are in a format that is useable without any manipulation.
