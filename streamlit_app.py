import streamlit
streamlit.title('My kids healthy Dinner')
streamlit.header('Dinner Menu')
streamlit.text(' 🥣 dosa')
streamlit.text('🥗 chutney')
streamlit.text('🐔 chicken fries')
streamlit.text('🥑🍞 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
