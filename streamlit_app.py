import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('SHPM')

def get_basic_info():
  with my_cnx.cursor(ssn_choice) as my_cur:
    my_cur.execute("select * from TMEM where SSN = ('" + ssn_choice + "')")
    return my_cur.fetchall()

streamlit.header("Enter SSN Here with No Dashes")
try:
  ssn_choice = streamlit.text_input('What is your SSN?')
  if not ssn_choice:
    streamlit.error("Please enter a SSN to get information.")
  else:
    back_from_function = get_ssn_info(ssn_choice)
    streamlit.dataframe(back_from_function)      

except URLError as e:
  streamlit.error()    

#streamlit.header("View Your Basic Information")
# Snowflake related functions
#def get_basic_info():
 # with my_cnx.cursor(ssn_choice) as my_cur:
  #     my_cur.execute("select * from TMEM where SSN = ('" + ssn_choice + "')")
   #    return my_cur.fetchall()
# Add a button to load fruit
#if streamlit.button('Get Basic Information'):
 #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  #my_data_rows = get_basic_info()
  #my_cnx.close()
  #streamlit.dataframe(my_data_rows)

# Allow end user to add a fruit to the list
#def insert_row_snowflake(new_fruit):
 # with my_cnx.cursor() as my_cur:
  #  my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
   # return "Thanks for adding " + new_fruit

#add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
#if streamlit.button('Add a Fruit to the List'):
 # my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 # back_from_function = insert_row_snowflake(add_my_fruit)
  #streamlit.text(back_from_function)
  #my_cnx.close()

#import streamlit
#import pandas
#import requests
#import snowflake.connector
#from urllib.error import URLError

#streamlit.title('SHPM')
#streamlit.header('Basic Information')
#streamlit.header("Enter SSN Here with No Dashes")
#try:
 # ssn_choice = streamlit.text_input('What is your SSN?')
  #if not ssn_choice:
   # streamlit.error("Please enter a SSN to get information.")
  #else:
   # back_from_function = get_ssn_info(ssn_choice)
    #streamlit.dataframe(back_from_function)      

#def get_ssn_info():
  #with my_cnx.cursor() as my_cur:
      # my_cur.execute("select * from TMEM where SSN = ('" + ssn_choice + "')")
       #return my_cur.fetchall()

#if streamlit.button('Get Basic Information'):
 # my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  #my_data_rows = get_ssn_info()
  #my_cnx.close()
  #streamlit.dataframe(my_data_rows)

#except URLError as e: 
 # streamlit.error()

# streamlit.header('Comments')
# streamlit.header('Dependents')
# streamlit.header('Coverage History')
# streamlit.header('Medicare Information')
# streamlit.header('Member Group Summary')
# streamlit.header('Direct Pay History')
# streamlit.header('Direct Premium Status')

streamlit.stop()
