import streamlit as st
import pandas as pd
import streamlit.components.v1 as com
import datetime
from datetime import date
import requests
import json
from email_validator import validate_email, EmailNotValidError
import deploy as dy      

st.set_page_config(page_icon="",
                   layout="centered",
                   initial_sidebar_state="expanded",
                   page_title="Website")
def main():
    st.title("My first streamlit web application")
    value = False #checks whether all the fields have been filled out
    num_years= 18 #the min age of the people attenting the hackathon
    menu = ["About", "Application"]
    choice = st.sidebar.selectbox("Menu of the application", menu)
    if choice == "About":
        # adds a specific subheader to each subpage
        st.subheader("About the competition")
        st.write("###### Navigate using the sidebar box to get to the application. Please ignore this site :)")
        ###########################################################################################
        #just playing around
        form1 = st.form(key="form_play")
        textarea= form1.text_area("What do you expect from this experience: (I am just trying this out)")
        button= form1.form_submit_button("Submit me")
        if button:
            st.success("Thank you for your suggestions!")

        video= st.video(data="https://youtu.be/HrNiCG5Izkc", format="video/mp4", start_time=0)
         ###########################################################################################
    elif choice == "Application":
        st.subheader("Application")
        st.write("### Just trying out whether using the link [works](https://www.google.com)")
        st.image("https://us.v-cdn.net/6036147/uploads/368UTZVITVZA/l-03-8-4-1200x675.jpg")
        with st.form(key="form", clear_on_submit=False):
            full_name = st.text_input("What is your full name: ", placeholder="Magda Trplan")
            #sets the time and puts a minimum value to it 
            dob = st.date_input("What is your date of birth: ", min_value=datetime.date(year= 1960, month=1, day=1), max_value=date.today() - datetime.timedelta(days= 365* num_years), value=datetime.date(year=2005,month=6, day=30))
            # Doing it like below would be far easier but the resulting code is not pretty at all :()
            #com.html("<input type='email' placeholder='type in your email address' required>")
            email = st.text_input("What is your email address: ", placeholder="Berger@ifo.de")
            ##########################################################################
            email_validity = True
            #checking for email validity
            try:
                check= validate_email(email)
            except EmailNotValidError:
                email_validity = False
            ##########################################################################

            cv = st.file_uploader("Attach your Resume: ", type="pdf")
            #st.set_option("deprecation.showfileUploaderEcoding", False)
            #cv = st.text_input("Just checking if it works this way")
            submit_button = st.form_submit_button("Click here to submit")
            #Checks whether all the input fields are non-empty
            all_fields = [full_name, email]
            boolean = True
            for entry in all_fields:
                if len(entry) == 0:
                    boolean=False
                    break
            if submit_button and boolean and email_validity:
                st.success("%s, you have submitted your application!" % (full_name))
                #here is where I upload the file
                file= cv.read()
                file_result= open(cv.name, "wb")
                file_result.write(file)
                file_result.close()
                name= cv.name
                path= "./"+name
                dy.get_drive(name, path)
                dy.input_info(full_name,email,dob)
            elif submit_button and (boolean==False and email_validity== True):
                st.error("Please fill in all the information")
            elif submit_button and (boolean==True and email_validity== False):
                st.error("Please type in the correct email address")
            elif submit_button and (boolean==False and email_validity== False):
                st.error("Please type in the correct email address and fill in all the information")
if __name__ == "__main__":
    main()
