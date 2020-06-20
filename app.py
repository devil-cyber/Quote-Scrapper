import os
import requests
from bs4 import BeautifulSoup
import streamlit as st



st.title('Web Scrapper')
st.subheader('Web Scrapper is a automation technology that provide you a way to extract data from the website')
search=st.text_input('Enter the Types of Quote You Like')
if st.button('Submit'):
    url=f'https://www.brainyquote.com/topics/{search}'
    r=requests.get(url)
    htmlcontent=r.content
    soup=BeautifulSoup(htmlcontent,'html.parser')
    q_list=soup.find_all('a',{'class':'b-qt'})
    if len(q_list)==0:
        st.write('You have entred wrong choice')
    else:
        for i in q_list:
            st.markdown(f"""<div style='background-color:greenyellow; border: 1px solid grey; color: red;margin-bottom:10px;width:100%; text-align: center;'>{i.text}</div>""", unsafe_allow_html=True)
         

 


 

 
