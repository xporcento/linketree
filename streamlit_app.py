import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

##st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('XPORCENTO_LOGO-positivo.jpg'))


st.header('X-PORCENTO')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

icon_size = 20

##st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
##st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
st_button('medium', 'https://medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/', 'Siga-nos no LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/', 'Buy me a Coffee', icon_size)
