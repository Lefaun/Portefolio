import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="Le Faun´s Portfolio",
    layout="wide"
)

# Define the CSS to hide Streamlit UI elements and set the background iframe
custom_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background: transparent;
    }
    .background {
        position: fixed;
        top: 0;
        left: 0%;
        height: 100%;
        width: 100%;
        z-index: -1;
        overflow: hidden;
    }
    .foreground {
        position: relative;
        z-index: 1;
    }
    .iframe {
        position: fixed;
        top: 0;
        left:0;
        height: 100%;
        width: 100%;
        border: none;
        z-index: -1;
    }
    @media (max-width:768px {
        .foreground {
            padding: 10px;
            align-items: center;
            color: white;
            
                }
       
    }
    .stApp {
        foreground: orange;
        }

    </style>
"""
# <iframe src="https://openprocessing.org/sketch/2065046/embed/"    width="100%" height="100%"></iframe>
#<iframe src="https://openprocessing.org/sketch/2065046/embed/"    width="100%" height="100%"></iframe>
#<iframe src="https://openprocessing.org/sketch/2284187/embed/" width="100%" height="100%"></iframe>
# HTML to embed the OpenProcessing iframe
openprocessing_iframe = """
    <div class="background">
        <iframe src="https://openprocessing.org/sketch/2257597/embed/" width="100%" height="100%"></iframe>
    </div>
"""

# Inject the CSS and HTML into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(openprocessing_iframe, unsafe_allow_html=True)

# Wrap your Streamlit content inside a div with the 'foreground' class
st.markdown('<div class="foreground">', unsafe_allow_html=True)

# Add your Streamlit menu here
st.image("logo.png")
st.image("subtile.png")
#st.markdown('<h1 class = title-mobile> O Le Faun´s Portfolio </h1>', unsafe_allow_html=True)
#st.write("DSIGN | WEB | 3D | GAME DESIGN | PYTHON")

# Create a sidebar menu
menu = st.sidebar.radio("Menu", ["Gallery 1", "Gallery 2", "Gallery 3"])

# Depending on the menu selection, show different galleries
if menu == "Gallery 1":
    cols = st.columns(3)
    with cols[0]:
        st.image("Dsign.png")
    with cols[1]:
        st.image("Web.png")
    with cols[2]:
        st.image("3D.png")
    cols = st.columns(3)    
    with cols[0]:
        st.image("5.png", caption="Image 1")
    with cols[1]:
        st.image("4.png", caption="Image 2")
    with cols[2]:
        st.image("10.png", caption="Image 2")
        
    cols = st.columns(2)
    with cols[0]:
        video_file = open('video1.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with cols[1]:
        video_filex = open('video2.mp4', 'rb')
        video_bytesx = video_filex.read()
        st.video(video_bytesx)
