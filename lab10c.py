import requests
import streamlit as stream
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html

stream.set_page_config(page_title="Lab10c - py/Streamlit", layout="wide")

def get_lottie (link):
    anim = requests.get(link)
    if anim.status_code == 200:
        return anim.json()
    else:
        return None

lotie = get_lottie("https://lottie.host/96a24526-44fa-4ea5-92ec-6321ac6478c5/BDDjkgXyM9.json")
lotie2 = get_lottie("https://lottie.host/4a78e05c-aa3e-46a0-85e6-95649adbf65e/QHXyAbXEZT.json")

dark = '''
<style>
    .stApp {
    background-color: black;
    color: white
    }

    #head {
    background-color: black;
    color: #ADD8E6}
</style>
'''

light = '''
<style>
    .stApp {
    background-color: white;
    color: black
    }
</style>
'''

stream.markdown(light, unsafe_allow_html=True)

with stream.container():
    lefttest_column, leftmost_column, left_column, middle_column, right_column, rightmost_column, rightest_column = stream.columns(7)
    with rightest_column:
        # Creating a toggle button
        toggle = stream.button("Change theme")

# Using a global variable to store the current theme
if "theme" not in stream.session_state:
    stream.session_state.theme = "light"

# Changing the theme based on current theme
if toggle:
    if stream.session_state.theme == "light":
        stream.session_state.theme = "dark"
    else:
        stream.session_state.theme = "light"

# Apply the theme to the app
if stream.session_state.theme == "dark":
    stream.markdown(dark, unsafe_allow_html=True)
else:
    stream.markdown(light, unsafe_allow_html=True)


with stream.container():
    lefttest_column, left_column, middle_column, right_column, rightest_column = stream.columns(5)
    with middle_column:
        stream.header("About me :wave:")
    stream.markdown("<span id=\"head\" style=\"font-size:40px\"><b>Hi, Welcome to my page. My name is Neel Faganiya</b></span>", unsafe_allow_html=True)
    stream.write("I am a 3rd year Computer Science student at Toronto Metropolitan University (formerly Ryerson University), and this is a simple webpage that I have created for one of my labs for Course: CPS530")
    stream.write("Click [here](https://www.cs.torontomu.ca/~nfaganiy/) to have a look at my other web development projects.")

with stream.container():
    stream.header("", divider="rainbow")
    left_column, right_column = stream.columns(2)
    with left_column:
        stream.markdown("<span id=\"head\" style=\"font-size:40px\"><b>How did I install the Framework?</b></span>", unsafe_allow_html=True)
        stream.write("##")
        stream.write(
            """
            First step towards installing the Streamlit framework was by creating an empty folder. Once that is done, open your code editor(preferably VScode). Then open a terminal, cd into the empty folder that you created
            . Then type the command "pip install streamlit" to install the framwork to your device. The next step is to create an empty .py file (in my case lab10c.py), in the same folder, to write the code for the website. Once you have written some 
            code in the .py file, open the terminal again(cd to the same directory) and type the command "streamlit run lab10c.py", NOTE: Change the name of the .py file from lab10c.py to whatever you named your file. Once that is done,
            it will automatically open a localhost for you with your webpage.
            """
        )
    
    with right_column:
        st_lottie(lotie, height=400)

with stream.container():
    stream.header("", divider="rainbow")
    left_column, right_column = stream.columns(2)
    with right_column:
        stream.markdown("<span id=\"head\" style=\"font-size:40px\"><b>How did I build this page?</b></span>", unsafe_allow_html=True)
        stream.write("##")
        stream.write(
            """
            This webpage consists of 3 sections. About me, installation of framework and how did I build this page. This page also has a toggle button at the top to change the theme of the page to Dark/Light. I built this webpage using Py/Streamlit, HTML, and CSS.
            Streamlit is the framework that I used to build this page. I have also used some basic HTML and CSS syntax, which was taught throughout the course, to give this page some design. I have also used lottiefiles to give an animation to this page.
            """
        )
    
    with left_column:
        st_lottie(lotie2, height=400)



with stream.container():
    stream.header("", divider="rainbow")
    left_column, middle_column, right_column = stream.columns(3)
    with middle_column:
        stream.markdown("<span id=\"head\" style=\"font-size:40px\"><b>Difficulties encountered</b></span>", unsafe_allow_html=True)
        stream.write("##")
        stream.write(
            """
            Some difficulties that I encountered while creating this webpage were: firstly, learning about this new framework, streamlit, that I have worked with while creating this page. Learning the basics, and the way to operate things
            with this new framework seemed a bit confusing at the start but with more and more practice and trying new things I got my hands around this and started understanding it really well. Then, importing the framework and its libraries
            ,for changing the theme on click/getting some animation on the webpage, took a bit of time but again, researching upon this eventully made it work at the end.
            """
        )

stream.write("##")
stream.write("##")
stream.markdown("<p style=\"font-family: 'Courier New', Courier, monospace; position:absolute; right:0\">Copyright © 2023 by Neel Faganiya. All rights reserved.</p>", unsafe_allow_html=True) 
    