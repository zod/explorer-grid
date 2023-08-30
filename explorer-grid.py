#!/usr/bin/env python

import mapbox_vector_tile

MIN_ZOOM = 11

MVT_EXTENT = 4096

# VeloViewer Explorer zoom level
GRID_ZOOM = 14
GRID_ITEMS = 2 ** (GRID_ZOOM - MIN_ZOOM)
GRID_STEP = MVT_EXTENT // GRID_ITEMS


def features():
    features = []
    for x in range(GRID_ITEMS):
        for y in range(GRID_ITEMS):
            coords = [
                (x * GRID_STEP, y * GRID_STEP),
                (x * GRID_STEP, (y + 1) * GRID_STEP),
                ((x + 1) * GRID_STEP, (y + 1) * GRID_STEP),
                ((x + 1) * GRID_STEP, y * GRID_STEP),
                (x * GRID_STEP, y * GRID_STEP),
            ]
            polygon = ", ".join(
                [" ".join([str(coordPart) for coordPart in coord]) for coord in coords]
            )
            wkt = f"POLYGON (({polygon}))"
            feature = {
                "geometry": wkt,
                "properties": {},
            }
            features.append(feature)
    return features


tileContent = {"name": "grid", "features": features()}

tile = mapbox_vector_tile.encode(tileContent)

with open("explorer-grid.mvt", "wb") as tileFile:
    tileFile.write(tile)
