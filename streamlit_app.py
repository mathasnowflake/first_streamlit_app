import streamlit
import pandas
import requests

import snowflake.connector
from urllib.error import URLError

streamlit.title('Jai Sri Rama')


streamlit.header('Jai Sri Rama Nama')

streamlit.text('Sri Rama')

streamlit.text(' Sri Rama')

streamlit.text(' Sri Rama')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Auocade Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New Section to display fruity vice api response


streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about ?')
  if not fruit_choice:
    streamlit.error("Please select a fruite to get information")
  else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
      #streamlit.text(fruityvice_response.json())
      # write your own comment -what does the next line do? 
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      # write your own comment - what does this do?
      streamlit.dataframe(fruityvice_normalized)
      
 except URLError as e:
      streamlit.error()
#fruit_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.stop()
#streamlit.dataframe(fruits_to_show)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.text("Hello from Snowflake: *JAI SRI RAMA*")
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_rows)
# Let's put a pick list here so they can pick the fruit they want to include 



title = streamlit.text_input('Add fruit', 'Jackfruit')
streamlit.write('Thanks for Adding Fruit', title)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values (''title'')")
#streamlit.text("Thanks for Adding Fruit: *JAI SRI RAMA*")
