# #!/usr/bin/env python
# # coding: utf-8
#
# # In[1]:
#
#
# # get_ipython().system('pip install area')
# # get_ipython().system('pip install wordcloud')
# # get_ipython().system('pip install geopandas')
# #
# #
# # # In[1]:
#
#
# #
# # import numpy as np # linear algebra
# # import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# # import seaborn as sns
# # import geopandas as gpd
# # import folium
# # import shapely.speedups
# # from folium.plugins import FastMarkerCluster
# # import plotly.graph_objects as go # or plotly.express as px
# # import matplotlib.pyplot as plt
# # import plotly.express as px
# # # import pandas_read_xml as pdx
# # import json
# # import math
# # from area import area
# # from sklearn import neighbors
# # from wordcloud import WordCloud, STOPWORDS
# # import re
# # from textblob import TextBlob
# # from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
# #
# #
# #
# # # Offline mode
# # from plotly.offline import init_notebook_mode
# # init_notebook_mode(connected=True)
# # from plotly.offline import iplot as ip
# #
# # import os
# # for dirname, _, filenames in os.walk('/kaggle/input'):
# #     for filename in filenames:
# #         print(os.path.join(dirname, filename))
# #
# #
# # # In[ ]:
# #
# #
# # # Data for Global Sea Levels
# # gsl = pd.read_csv('sea-level-change/sea_levels_2015.csv', error_bad_lines=False)
# #
# #
# # # In[ ]:
# #
# #
# # # Global Sea Level
# # gsl_data = go.Scatter(x=gsl['Time'],y=gsl['GMSL'])
# # gsl_data_1 = go.Scatter(x=gsl['Time'],y=gsl['GMSL uncertainty'])
# #
# # layout = go.Layout(title='Rising Global Sea Levels', title_x=0.5, xaxis=dict(title='Year'),yaxis=dict(title='Global Mean Sea Level (GMSL) (mm)'),template='plotly_dark')
# # fig = go.Figure(layout=layout)
# # fig.add_trace(go.Scatter(
# #    x=gsl['Time'],y=gsl['GMSL'],
# #     name="GMSL"
# # ))
# # fig.add_trace(go.Scatter(
# #    x=gsl['Time'],y=gsl['GMSL uncertainty'],
# #     name="GMSL Uncertainty"
# # ))
# # ip(fig)
#
#
# # In[3]:
#
#
# # get_ipython().system('pip install geopandas')
# #
# #
# # # In[ ]:
# #
# #
# # get_ipython().system('python')
# #
# #
# # # In[2]:
# #
# #
# # url1 = 'https://tidesandcurrents.noaa.gov/sltrends/downloadMeanSeaLevelTrendsCSV.ht'
# # url2 = 'm;jsessionid=D79899A1D9FCE54F6DC6A107F9439C5D?stnid=8518750'
# # url = url1 + url2
# # clvl = pd.read_csv(url)
# # # Creating the four section by slicing the dataset
# # t1 = clvl[:612]
# # t2 = clvl[612:1212]
# # t3 = clvl[1212:1716]
# # t4 = clvl[1716:1994]
# # # Calculating the trends for each section; We calculate the trend from difference as our data represents
# # # Note: In this dataset the column label Linear_Trend is preceded by a black space so we must use ' Linear_Trend when calling the data.
# # dif1 = clvl[' Linear_Trend'][611] - clvl[' Linear_Trend'][0]
# # dif2 = clvl[' Linear_Trend'][1211] - clvl[' Linear_Trend'][612]
# # dif3 = clvl[' Linear_Trend'][1715] - clvl[' Linear_Trend'][1212]
# # dif4 = clvl[' Linear_Trend'][1993] - clvl[' Linear_Trend'][1716]
# # trend1 = dif1 / len(t1[' Linear_Trend'])
# # trend2 = dif2 / len(t2[' Linear_Trend'])
# # trend3 = dif3 / len(t3[' Linear_Trend'])
# # trend4 = dif4 / len(t4[' Linear_Trend'])
# #
# #
# # # In[4]:
# #
# #
# # import pandas as pd
# # from matplotlib import pyplot as plt
# # from matplotlib.animation import FuncAnimation
# # import cartopy.crs as ccrs
# # from cartopy.feature import NaturalEarthFeature
# # import xarray as xr
# #
# # xr_df = xr.open_dataset('gistemp1200_GHCNv4_ERSSTv5.nc.gz')
# # xr_df
# #
# #
# # # In[5]:
# #
# #
# # #Downsample the time series to yearly frequency.
# # climate = xr_df.resample(time='Y').mean()
# # anomaly = climate['tempanomaly']
# #
# # #Creating a static image of the global temperature anomaly for a given year.
# # cbar_kwargs = {
# #     'orientation':'horizontal',
# #     'fraction': 0.045,
# #     'pad': 0.01,
# #     'extend':'neither'
# # }
# #
# # fig = plt.figure(figsize=(20,20))
# # ax = fig.add_subplot(1,1,1, projection = ccrs.PlateCarree())
# # ax.add_feature(NaturalEarthFeature('cultural', 'admin_0_countries', '10m'),
# #                        facecolor='none', edgecolor='black')
# # ax.set_extent([-150, 150, -55, 85])
# #
# # i=-1
# # date =  pd.to_datetime(anomaly.isel(time=i)['time'].values)
# # ax.set_title("Temperature Anomaly in "+ str(date.year) + " [°C]")
# # anomaly.isel(time=i).plot.imshow(ax=ax, add_labels=False, add_colorbar=True,
# #                vmin=-4, vmax=4, cmap='coolwarm',
# #                cbar_kwargs=cbar_kwargs, interpolation='bicubic')
# # plt.savefig("global_map.png", bbox_inches='tight', dpi=150)
# # plt.show()
# #
# #
# # # In[34]:
# #
# #
# #
# # #Creating a static image of the european temperature anomaly for a given year.
# # cbar_kwargs = {
# #     'orientation':'horizontal',
# #     'fraction': 0.048,
# #     'pad': 0.01,
# #     'extend':'neither'
# # }
# #
# # fig = plt.figure(figsize=(15,10))
# # ax = fig.add_subplot(1,1,1, projection = ccrs.PlateCarree())
# # ax.add_feature(NaturalEarthFeature('cultural', 'admin_0_countries', '10m'),
# #                        facecolor='none', edgecolor='black')
# # ax.set_extent([-11, 41, 34, 71])
# # i=-1
# # date =  pd.to_datetime(anomaly.isel(time=i)['time'].values)
# # ax.set_title("Temperature Anomaly in "+ str(date.year) + " [°C]")
# # xr.plot.imshow(anomaly.isel(time=i), ax=ax, add_labels=False,
# #                    vmin=-4, vmax=4, cmap='coolwarm',
# #                    cbar_kwargs=cbar_kwargs, interpolation='bicubic')
# # plt.savefig("european_map.png", bbox_inches='tight', dpi=150)
# # plt.show()
# #
# #
# # # In[32]:
# #
# #
# # # Creating an animation for 1950-2020 and saving it as an MP4 video.
# # cbar_kwargs = {
# #     'orientation':'horizontal',
# #     'fraction': 0.048,
# #     'pad': 0.01,
# #     'extend':'neither'
# # }
# #
# # fig = plt.figure(figsize=(20,20))
# # fig.subplots_adjust(left=0.02, bottom=0.04, right=0.98, top=0.96)
# # ax = fig.add_subplot(1,1,1, projection = ccrs.PlateCarree())
# # ax.add_feature(NaturalEarthFeature('cultural', 'admin_0_countries', '10m'),
# #               facecolor='none', edgecolor='black')
# # ax.set_extent([-11, 91, 34, 71])
# #
# # image = anomaly.isel(time=0).plot.imshow(ax=ax, add_labels=False,
# #                        vmin=-4, vmax=4, cmap='coolwarm', animated=True,
# #                        cbar_kwargs=cbar_kwargs, interpolation='bicubic')
# #
# # def animate(t):
# #     date =  pd.to_datetime(anomaly.sel(time=t)['time'].values)
# #     ax.set_title("Temperature Anomaly in " + str(date.year) + " [°C]")
# #     ax.title.set_fontsize(18)
# #     image.set_array(anomaly.sel(time=t))
# #     return image
# #
# # ani = FuncAnimation(fig, animate, frames=anomaly['time'].values[-71:], blit=False)
# # # writergif = ani.PillowWriter(fps=30)
# # # ani.save('filename.gif',writer=writergif)
# # ani.save("animation.gif", fps=2) #, extra_args=['-vcodec','libx264', '-crf','15', '-preset','veryslow'])
# #
# #
# # # In[23]:
#
# import pandas as pd
# from matplotlib import pyplot as plt
# from matplotlib.animation import FuncAnimation
# import cartopy.crs as ccrs
# from cartopy.feature import NaturalEarthFeature
# import xarray as xr
#
# xr_df = xr.open_dataset('gistemp1200_GHCNv4_ERSSTv5.nc.gz')
# xr_df
# import pandas as pd
# # Data for Global Sea Levels
# gsl = pd.read_csv('sea_levels_2015.csv', error_bad_lines=False)
#
#
# # In[26]:
#
#
# import plotly.offline as py
# import plotly.graph_objs as go
# gsl_data = go.Scatter(x=gsl['Time'],y=gsl['GMSL'])
# gsl_data_1 = go.Scatter(x=gsl['Time'],y=gsl['GMSL uncertainty'])
# price = go.Scatter(x=gsl['Time'],y=gsl['GMSL uncertainty'],name="GMSL Uncertainty")
# py.iplot([price])
#
#
# # In[29]:
#
#
# from plotly.offline import iplot as ip
#
# layout = go.Layout(title='Rising Global Sea Levels', title_x=0.5, xaxis=dict(title='Year'),yaxis=dict(title='Global Mean Sea Level (GMSL) (mm)'),template='plotly_dark')
# fig = go.Figure(layout=layout)
# fig.add_trace(go.Scatter(
#    x=gsl['Time'],y=gsl['GMSL'],
#     name="GMSL"
# ))
# fig.add_trace(go.Scatter(
#    x=gsl['Time'],y=gsl['GMSL uncertainty'],
#     name="GMSL Uncertainty"
# ))
# ip(fig)
# # # fig.save("hello.png")
# # print(fig)
#
#
# # In[31]:
#
#
# climate = xr_df.resample(time='Y').mean()
# anomaly = climate['tempanomaly']
# layout = go.Layout(title='Rising Global Sea Levels', title_x=0.5, xaxis=dict(title='Year'),yaxis=dict(title='Global Mean Sea Level (GMSL) (mm)'),template='plotly_dark')
# fig = go.Figure(layout=layout)
# fig.add_trace(go.Scatter(
#    x=gsl['Time'],y=gsl['GMSL'],
#     name="GMSL"
# ))
# fig.add_trace(go.Scatter(
#    x=xr_df['time'],y=xr_df['tempanomaly'],
#     name="Temp"
# ))
# ip(fig)
#
#
# # In[ ]:
#
#
# # plt.title("Global Land and Ocean Temperature Anomalies, June")
# # plt.xlabel('‘year’')
# # plt.ylabel('degrees F +/- from average')
# # plt.bar(data[‘date’], data[‘value’], color=”blue”)
# # plt.show()
#

# Data for Global Sea Levels
from plotly.offline import iplot as ip
import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt
gsl = pd.read_csv('sea_levels_2015.csv')
def plot():
    layout = go.Layout(title='Rising Global Sea Levels', title_x=0.5, xaxis=dict(title='Year'),yaxis=dict(title='Global Mean Sea Level (GMSL) (mm)'),template='plotly_dark')
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(
       x=gsl['Time'],y=gsl['GMSL'],
        name="GMSL"
    ))
    fig.add_trace(go.Scatter(
       x=gsl['Time'],y=gsl['GMSL uncertainty'],
        name="GMSL Uncertainty"
    ))
    plt.scatter(x=gsl['Time'],y=gsl['GMSL'])
    plt.title("Scatter")
    plt.title("Rising Global Sea Levels")
    plt.xlabel('Year')
    plt.ylabel('Global Mean Sea Level (GMSL) (mm)')
    plt.savefig("Scatter.png", facecolor='white',
                transparent=True, bbox_inches='tight')
    # plt.savefig(('GMSL.png'),facecolor='white', transparent=True, bbox_inches='tight')

    plt.close()
    # ip(fig)
    print("Hello")
    # plt.plot(fig)
    # fig.write_image(file='GMSL.png')
plot()
