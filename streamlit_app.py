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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include  
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("The Fruit load list contains:")
streamlit.header("The Fruit load list contains:")
# streamlit.text(my_data_row)
streamlit.dataframe(my_data_rows)

streamlit.header("what fruit would you like to add:")
add_my_fruit_response = ("Jackfruit")
streamlit.text(add_my_fruit_response)
streamlit.text("Thanks for adding jackfruit")
