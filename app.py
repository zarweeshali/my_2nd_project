import streamlit as st

st.title("Personal Library Manager with Recommendation!" )
st.write(" ### + Add a New Book")
first_name = st.text_input ("Enter the Book Name")
first_name = st.text_input ("Enter the Author Name")
first_name = st.text_input ("Book Price")
first_name = st.text_input ("Book Quality")
first_name = st.text_input ("Book Genre")
st.checkbox("Have you read this book?")
def count_down():
    if st.button("Add Book"):
        return st.success("Book added Successfully!")
    
count_down()
st.balloons()
st.sidebar.header("Welcome to library")
st.sidebar.text("Menu")
st.sidebar.selectbox("+ Add a Book", {"Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics"})
 




  


