import geopandas as gpd
import os
import argparse

def regular_polygon_to_point(polygon_uri):
	gdf = gpd.read_file(polygon_uri)
	geom = gdf.geometry
	centroids = geom.centroid
	pt_gdf = gdf
	pt_gdf['geometry'] = centroids
	outname = polygon_uri.split('.')[0] + '_pts' + '.shp'
	pt_gdf.to_file(outname)
	return(None)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('polygon_uri')
    args = parser.parse_args()
    regular_polygon_to_point(args.polygon_uri)
