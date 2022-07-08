import time
from tracemalloc import Snapshot  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from PIL import Image



st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="🎈",
    layout="wide",
)

def main():
    url = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
    @st.experimental_memo
    def get_data() -> pd.DataFrame:
        return pd.read_csv(url)

    df = get_data()

    st.title("SpaceX launch Dashboard")
    image = Image.open('rocket_launch.jpg')
    st.image(image)
    st.sidebar.markdown("## WINNING SPACE RACE WITH DATA SCIENCE")
    st.sidebar.markdown("""The understanding of harnessing data has revealed lots of insights that has 
    helped companies in making right future decisions. Use of Data science techniques 
    (from the analysis of data to its evaluation to machine learning prediction) will help us 
    to achieve the goal of this project which is to predict the outcome of the first landing of 
    Falcon9 Rocket. This is needed as it will help our company determine the ideal cost of a 
    launch and also the working principles behind SpaceX successful reuse of the first stage 
    of launch.
    The data will reveal to us the factors that ultimately has an effect on the 
    outcome of the launch ,this determining factors(variables) will be compared with the 
    outcome and trends will be extracted which will be used to predict the outcome of a 
    launch in the future and also inform the company of the right conditions to be put in 
    place for a successful launcThe understanding of harnessing data has revealed lots of insights that has 
    helped companies in making right future decisions. Use of Data science techniques 
    (from the analysis of data to its evaluation to machine learning prediction) will help us 
    to achieve the goal of this project which is to predict the outcome of the first landing of 
    Falcon9 Rocket. This is needed as it will help our company determine the ideal cost of a 
    launch and also the working principles behind SpaceX successful reuse of the first stage 
    of launch.
    The data will reveal to us the factors that ultimately has an effect on the 
    outcome of the launch ,this determining factors(variables) will be compared with the 
    outcome and trends will be extracted which will be used to predict the outcome of a 
    launch in the future and also inform the company of the right conditions to be put in 
    place for a successful launch""")


    st.markdown("### Payload Mass (kg) per Launch Site")
    # line chart 
    # Use directly Columns as argument. You can use tab completion for this!
    figa = px.scatter(df, x=df.PayloadMass, y=df.LaunchSite, color=df.LaunchSite, size=df.PayloadMass)
    figa.show()
    st.write(figa)
    st.markdown("Now if you observe Payload Vs. Launch Site scatter point chart you will find for the VAFB-SLC  launchsite there are no  rockets  launched for  heavypayload mass(greater than 10000).")
    

    # create two columns for charts
    st.markdown("### Pie Chart showing Launch Site with the highest Success Rate")
    orbitt = df.groupby('LaunchSite').mean()
    orbitt.reset_index(inplace=True)    
    fig = px.pie(orbitt, names ='LaunchSite' , values= 'Class')
    fig.show()
    st.write(fig)
    st.markdown("KSC LC 39A is seen to be the launch site with the highest success rate")

    st.markdown("### Bar Chart showing the Succcess outcome with respect to Orbit")
    mean = df.groupby('Orbit').mean()
    mean.reset_index(inplace= True)
    fig2 = px.bar(mean, x ='Orbit', y='Class', color='Class',
    labels={'Orbit':'Orbit Success rate'}, height=400)
    fig2.show()
    st.write(fig2)
    st.markdown(" Orbits : ES-L1, GEO, HEO, SSO have more success launch rate")


    st.markdown("### Detailed Data View")
    st.dataframe(df)
            
if __name__ == '__main__':
    main()
    






    
