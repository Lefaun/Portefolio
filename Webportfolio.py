from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib as plt
from collections import Counter
# Streamlit layout configuration
st.set_page_config(
    page_title="OpenProcessing Background",
    page_icon="🎨",
    layout="wide",
)

custom_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {background: transparent; position: relative; z-index: -3;}
    .background {
        position: fixed;
        top: 0;
        
        left: 0;
        height: 100%;
        width: 100%;
        z-index: -1;
        overflow: hidden;
        background: transparent;
    }
    .foreground {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.8); 
        
    }
    .iframe {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        z-index: -2;
    
        
    }
    </style>
"""


openprocessing_iframe = """
    <div class="background">
      <iframe src="https://openprocessing.org/sketch/2275356/embed/"  style="border:0" width="100%" height="100%"></iframe>
    </div>
"""
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)



st.title("                        O MEU PORTFOLIO")
#Open Processing 2

# Hide the default Streamlit style


image=[ {"name": "2.png", "likes": 0},{"name": "3.png", "likes": 0},{"name": "Sonia Monteiro Imobiliary.png", "likes": 0},{"name": "star.png", "likes": 0}]

# Create an empty dictionary to store the number of likes per day of the week
likes_per_day = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
days_of_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

# Create a list to store the likes per day of the week
likes_per_day = [0, 0, 0, 0, 0, 0, 0]

# Create a list to store the date of the like
date_likes = []

now=[]
# Create a function to display the histogram of likes per day of the week
st.title("                        O MEU PORTFOLIO")

st.title("                        O MEU PORTFOLIO")





def main():
    st.set_page_config(page_title="O MEU PORTEFOLIO", page_icon=":guardsman:", layout="centered")

    # 2. horizontal menu
selected2 = option_menu(None, ["Home", "About Me", "Art", "Design", "Video", "3D", "IoT", "Graphics"],
    icons=None,
    default_index=0, orientation="horizontal")

    # 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", (["Home", 'Settings', 'Dashboard 1', 'Dashboard2']),menu_icon="cast", default_index=1 )
                        #icons=['house', 'gear'],

# Create the responsive menu


st.markdown('<div class="foreground">', unsafe_allow_html=True)
st.markdown(openprocessing_iframe, unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)

def display_menu():
    menu = ["Home", "About", "Art", "Design", "Video", "3D", "IoT", "Graphics"]
    choice = st.selectbox("Select an option", menu)
    if choice == "Home":
        st.title("Welcome to My Gallery")
        st.write("This is a sample application to showcase a gallery of images and a chart of likes per day of the week.")
    elif choice == "About":
        st.title("About Me")
        st.write("My name is Streamlit and I love to create web applications.")
    elif choice == "Art":
        st.title("About Me")
        st.write("My name is Streamlit and I love to create web applications.")
        display_images("Art")
    elif choice == "Design":
        st.title("About Me")
        st.write("My name is Streamlit and I love to create web applications.")

        # Allow only .csv and .xlsx files to be uploaded

        chart_data = st.file_uploader("Upload spreadsheet", type=["csv", "xlsx"])

        # Check if file was uploaded
        if chart_data:
            # Check MIME type of the uploaded file
            if chart_data.type == "text/csv":
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            # Work with the dataframe
            st.dataframe(df.head())

    elif choice == "Video":
        st.title("About Me")
        st.write("My name is Streamlit and I love to create web applications.")
        display_images("Video")
    elif choice == "3D":
        st.title("About Me")
        st.write("My name is Streamlit and I love to create web applications.")
        display_images("3D")
    elif choice == "IoT":
        st.title("About Me")
        st.write("My name is Streamlit and I love to create web applications.")
        chart_data = pd.read_csv('Topicosbem.csv', sep=',')
        # Work with the dataframe
        st.dataframe(chart_data.head(15))
        columns = (['Length', 'Height', 'Width', 'Frequency', 'Word', ])

        chart_data = pd.DataFrame(
            np.random.randn(20, 5),
            columns=['Length', 'Height', 'Width', 'Frequency', 'Word'])
        st.bar_chart(chart_data)

        chart_data = pd.DataFrame(
            np.random.randn(20, 5),
            columns=['Length', 'Height', 'Width', 'Frequency', 'Word'])

        c = alt.Chart(chart_data).mark_circle().encode(
            x='Length', y='Frequency', size='Height', color='Word',
            tooltip=['Length', 'Height', 'Width', 'Frequency', 'Word'])

        st.altair_chart(c, use_container_width=True)


    elif choice == "Graphics":
        st.title("About Me")
        st.write("My name is Streamlit and I love to create web applications.")
        display_images("Graphics")
    elif choice == 'Dashboard 1':
        st.title('Dashboard 1')
        volume = [350, 220, 170, 150, 50]
        labels = ['Liquid\n volume: 350k', 'Savoury\n volume: 220k',
        'Sugar\n volume: 170k', 'Frozen\n volume: 150k',
        'Non-food\n volume: 50k']
        color_list = ['#0f7216', '#b2790c', '#ffe9a3',
        '#f9d4d4', '#d35158', '#ea3033']

        plt.rc('font', size=14)
        squarify.plot(sizes=volume, label=labels,
        color=color_list, alpha=0.7)
        plt.axis('off')
        st.pyplot()
display_menu()

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Video")
   st.image ("3.png")
   button_1 = st.button("Gosto", key="abnormal")
with col2:
   st.header("Design")
   st.image("2.png")

   button_2 = st.button("Gosto", key="cool")
with col3:
   st.header("ART")
   st.image("2.png")
   button_3 = st.button("Gosto", key="psy ")



