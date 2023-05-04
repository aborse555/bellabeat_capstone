import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('SHPM')

def get_ssn_info(ssn_choice):
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from TMEM where SSN = ('" + ssn_choice + "')")
       return my_cur.fetchall()
  
my_ssn = streamlit.text_input('What is your SSN?')
if streamlit.button('Get Basic Information'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = get_ssn_info(my_ssn)
  streamlit.text(back_from_function)
  my_cnx.close()

#if streamlit.button('Get Basic Information'):
#  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 # my_data_rows = get_ssn_info()
  #my_cnx.close()
  #streamlit.dataframe(my_data_rows)

#streamlit.header("Enter SSN Here with No Dashes")
#try:
 # ssn_choice = streamlit.text_input('What is your SSN?')
  #if not ssn_choice:
   # streamlit.error("Please enter a SSN to get information.")
  #else:
   # back_from_function = get_ssn_info(ssn_choice)
    #streamlit.dataframe(back_from_function)      
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
