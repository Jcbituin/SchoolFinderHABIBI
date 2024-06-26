from PIL import Image
import streamlit as st

# ---- LOAD ASSETS ----
image1 = Image.open("image/GG.png")

st.title("SCHOOL FINDER HUB")

# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    st.header("Bituin's Blog")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image1)
    with text_column:
        st.subheader("Hi It's me James Carl :wave:")
        st.write(
            """
            Right now I'm making my blog about my life, cause this is my project for our major subject in Computer Engineering
            """
        )
        st.write("I hope you like it!!!")


