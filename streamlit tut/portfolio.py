import streamlit as st
import pandas as pd
import numpy as np


my_container = st.container()
st.sidebar.image("mylogo.png")




sidebar_selection = st.sidebar.selectbox("Main Menu:", ['Home', 'work experience', 'Projects', 'Blog', 'My Archive',  'Contact'])

if sidebar_selection =="Home":
        with st.container():
            st.markdown("# WELCOME TO MY PORTFOLIO.")
            st.write("_____________________________________________")
            part1, part2 = st.columns(2)
        with part1:
            st.markdown("# I' am Eric Ocaya")
            st.markdown("#### I' am a UI/UX designer")
            st.markdown("#### I' am a data analyst. ")
            st.markdown("#### I' am a CCTV expert ")
            st.markdown("#### I' am a Web developer ")
            st.markdown("#### I' am a photographer ")
            st.markdown("#### Infact I am Tech ")
            st.markdown("####  So Tech with me")
            
        with part2:
            st.image("cover.png")
            st.markdown("### Brief Intro:")
            st.write("Born  and raised in Gulu, a native of paduny lamogi, Anaka town council, Nwoya district in Northern Uganda. Studied in Gulu public primary school, Holy rosary P. 7 school, Gulu High school, Atapara SSS and Gulu University.")
            st.markdown("### My Objectives:")
            st.write("- To achieve the goals and objectives of the company ")
            st.write("- To add value to company or organization")
            st.write("- To be a good leader or member of any project")
        st.write("___________________________________________________")
        st.markdown("### My tools")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.write("Python")
            st.image("python.png")
            st.write("Streamlit")
            st.image("streamlit2.png")
            st.write("Django")
            st.image("django.png")
            
        with col2:
            st.write("PhP")
            st.image("php.png")
            st.write("Adobe photoshop")
            st.image("photoshop.png")
            st.write("R")
            st.image("r.png")
        with col3:
            st.write("MsQL")
            st.image("mysql.png")
            st.write("Adobe premier pro cc")
            st.image("premier.png")
            st.write("VS code")
            st.image("vscode.png")
        with col4:
            st.write("React")
            st.image("react.png")
            st.write("Blender")
            st.image("blender.png")
            st.write("FL Studio")
            st.image("flstudio.png")
        st.write("___________________________________________________")
        st.write("@ All rights reserved. copyright @ eric ocaya.")
        
        
        
       
   
elif sidebar_selection =="work experience":
        st.header("work experience.")
        st.write("___________________________________________________")
        st.info("Click the button below to view work experience")
        with st.container():
                if st.button("Click here "):
                        st.image("work exp.png")
               
                      
                else:
                        st. write("Just click on the button")
        
            
          
            
elif sidebar_selection =="Projects":
    st.markdown("## My projects.")
    st.write("___________________________________________________")
    st.warning("### ! No project available at the moment.")
    st.markdown("#### Complete projects will be uploaded soon..........")
 
elif sidebar_selection =="Blog":
    st.markdown("## Post something here!")
    st.write("___________________________________________________")
    post1, post2 = st.columns(2)
    with post1:
        st.image("myimage.png")
    with post2:
        st.markdown("## Whats on your mind?")
        st.text_input("Please enter your email.",placeholder ="Email eg. johndoe@gmail.com")
        st.text_input("Enter your cell phone or Telephone number ",placeholder ="eg. 0712345678")
        st.text_area("comment", placeholder = "Text here...")
        st.button("Submit")
    st.write("___________________________________________________")
    st.write("@ All rights reserved. copyright @ eric ocaya.")
elif sidebar_selection =="My Archive":
        
        st.header("Welcome to my document center")
        menu = st.radio('Choose what do you want to view?', ['Documents', 'Photos'])
     
        if menu =="Documents":
                st.header("Documents will be available soon...")
        elif menu =="Photos":
                st.image("caro.jpg")
                st.image("group.jpg")
                st.image("farm.jpg")
                st.image("cap.jpg")

                        
        

elif sidebar_selection =="Contact":
    st.markdown("## Contact me any time anywhere!")
    st.write("___________________________________________________")
    col1, col2,col3= st.columns(3)
    with col1:
        st.image("mobile.png")
        st.image("whatsapp.png")
        st.image("utube.png")
    with col3:
        st.markdown("##### MTN: +256 788796748")
        st.markdown("##### MTN: +256 762176600")
        st.markdown("#####  Airtel:...................")
        st.write("Email: ericsonocaya@gmail.com")
        st.markdown("##### Tiktok: @ballboy")
        st.write("___________________________________________________")
        st.markdown("##### whatsapp: 0788796748")
        st.markdown("### ")
        st.markdown("### ")
        st.write("___________________________________________________")
        st.markdown("##### Channel: Nwoya wahala TV")
        st.markdown("##### Youtube Link: @Zxkslihsksg.com")
    st.write("___________________________________________________")
    st.write("@ All rights reserved. copyright @ eric ocaya.")

                
      
       
        

            


