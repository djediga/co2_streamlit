#import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

st.title('Co2 Emission per Country')

co2_df = pd.read_csv("../../data/CO2_per_capita.csv", sep=";")


#bar chart
def top_n_emitters(df, start_year=2008, end_year=2011, nb_displayed=10):
    
    #years filter
    mask = (df['Year']>=start_year) & (df['Year'] <= end_year)
    df_filtered =df[mask]
    # do the mean for each country
    df_filtered_mean = df_filtered.groupby('Country Name')['CO2 Per Capita (metric tons)'].mean()
    df_filtered_mean = df_filtered_mean.reset_index()
    
    #sort the values and keep nb_displayed
    df_sorted = df_filtered_mean.sort_values(by='CO2 Per Capita (metric tons)', ascending=False)

    df_top = df_sorted.head(nb_displayed)
   
    
    
    #create the fig
    fig = px.bar(df_top, x = 'Country Name', y = 'CO2 Per Capita (metric tons)')

    
    #return the fig
    return fig

start_year, end_year = st.slider('choose years',  min_value=1970, max_value=2011,value=(2000, 2011))
n = st.selectbox("Select number of country to diplay", [3,5,10,20,30], index=2)

fig = top_n_emitters(co2_df, start_year, end_year, n)

st.plotly_chart(fig)


st.header('Maps')
## TODO: Visualize your data on a World map
co2_df= co2_df.dropna().sort_values('Year')
#
## TODO: Visualize your data on a World map
fig = px.scatter_geo(co2_df, locations="Country Code",
                    # color="continent", # which column to use to set the color of markers
                    hover_name="Country Name", # column added to hover information
                    size="CO2 Per Capita (metric tons)", # size of markers
                    animation_frame='Year')
st.plotly_chart(fig)