import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=400)

with col2:
    st.title("Ivan Dantsevich")
    content = """Hi, I'm Ivan. I'm a self-motivated Full-Stack Developer with 3 years of experience building products 
    for a U.S. client. I specialize in Python and have a strong background in backend development and architecture. 
    I've completed advanced courses to improve my skills, and I also have experience in product management, 
    focusing on creating user-centered solutions that align with business needs."""
    st.info(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
