#!/usr/bin/env python

import mapbox_vector_tile

MVT_EXTENT = 4096

tile = mapbox_vector_tile.encode(
    {
        "name": "explorer",
        "features": [
            {
                "geometry": f"POLYGON ((0 0, 0 {MVT_EXTENT}, {MVT_EXTENT} {MVT_EXTENT}, {MVT_EXTENT} 0, 0 0))",
                "properties": {},
            }
        ],
    },
)

with open("explorer-grid.mvt", "wb") as tileFile:
    tileFile.write(tile)