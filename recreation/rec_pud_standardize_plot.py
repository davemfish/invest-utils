# Usage:
# python rec_pud_standardize_plot.py path/to/pud_results.shp
# or import this module to expose the functions

import geopandas as gpd
import pandas as pd
import numpy as np
import os
# import matplotlib as mpl
import matplotlib.pyplot as plt
import argparse
plt.rcParams['axes.facecolor']='white'


def plot_standardized_pud(pud_shp_4plot):
    """
    Make a plot using the pud_prsqrt variable created by pud_standardize_01()
    Parameters: pud_shp_4plot (string) : uri of pud shapefile output created by pud_standardize_01()
    """
    shp = gpd.read_file(pud_shp_4plot)

    # Create a figure of the desired size:
    fig = plt.figure(figsize=(10,10))  
    ax = plt.axes()
    ax.set_aspect('equal')
    ax.grid(False)
    plt.tick_params(
        axis='both',
        which='both', 
        right='off',
        left='off',
        bottom='off',
        top='off',
        labelbottom='off',
        labelleft='off') 

#     plt.suptitle(metadata['parkname'], fontsize=16)
#     plt.title(metadata['parkvis'], fontsize=14)
#     fig.text(.12,.08,metadata['cellsize'], fontsize=12)
    
    cmap = plt.cm.viridis
    cmap.set_under(color='dimgray')
    plot = shp.plot(ax=ax, 
                    column = 'pud_prsqrt',
                    cmap = cmap, 
                    vmin=0.0000001,
                    edgecolor='none',
                    k=7,
                    legend = True)
    
    pngname = pud_shp_4plot.split('.')[0] + '.png'
    plt.savefig(pngname)
    plt.close(plt.gcf())
    return(0)

def pud_standardize_01(pud_results_shp, pud_variable='PUD_YR_AVG'):
    """
    Transform the highly right-skewed PUD count variable in a way that is optimized for mapping.
    First make a PUD value that is the proportion of the sum of all PUDs. 
    Then sqrt transform that proportional value to emphasize variation in the low end.
    Parameters: pud_results_shp (string) : uri of pud shapefile output
                pud_variable (string) : column name in the pud_results_shp table
    """
    gdf = gpd.read_file(pud_results_shp)
    gdf['pud_pr'] = gdf[pud_variable] / np.sum(gdf[pud_variable])
    gdf['pud_prsqrt'] = np.sqrt(gdf['pud_pr'])
    
    outname = pud_results_shp.split('.')[0] + '_4plot' + '.shp'
    gdf.to_file(outname)

    plot_standardized_pud(outname)

    return(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('pud_results_path')
    parser.add_argument('--pud_var', help='Name of the pud variable to transform. None defaults to PUD_YR_AVG')
    args = parser.parse_args()
    if args.pud_var:
        pud_standardize_01(args.pud_results_path, args.pud_var)
    else:
        pud_standardize_01(args.pud_results_path)