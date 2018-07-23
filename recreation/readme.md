#### rec_pud_standardize_plot.py
Transform the highly right-skewed PUD count variable in a way that is optimized for mapping.
First make a PUD value that is the proportion of the sum of all PUDs. 
Then sqrt transform that proportional value to emphasize variation in the low end.

#### invest_pud_pr.qml
A style file for QGIS to symbolize the pud_pr variable in the shapefile created by rec_pud_standardize_plot.py

#### rec_pud_polygon_to_point.py
Converts polygon shapefile to point shapefile, using polygon centroids. 

#### invest_pud_pr_points.qml  
A style file for QGIS to symbolize the pud_pr variable in the shapefile created by rec_pud_standardize_plot.py and then converted to points using rec_pud_polygon_to_point.py

#### recmodel_client_parameters_boilerplate.py
sample script to call InVEST rec model

#### rec_monthlytable_wide2long.py
reshape the monthly_table.csv output from invest. The table comes in wide format, but long is often better-suited for aggregations and plotting.

#### pud_style_legends.svg & pud_style_legends.png
![](https://raw.githubusercontent.com/davemfish/invest-utils/master/recreation/pud_style_legends.png)
