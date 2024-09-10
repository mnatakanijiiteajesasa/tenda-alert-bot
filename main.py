import streamlit as st
from scrape import scrape_tenders
from tender_email_csv import save_tenders_to_csv, send_email_with_csv
from ai import filter_tenders_huggingface
import pandas as pd

# SMTP Configuration
from_email = "mogakanewton0@gmail.com"
password = "replace_with_your_password"
to_email = "mogakanewton0@outlook.com"
subject = "Tender Summary"
body = " Hello!\n Attached is your daily list of new government tenders. Feel free to check them out ☺️ :"
csv_file_path = "./tenders.csv"

# websites to scrape
st.title("Tender Alert")
websites = st.text_input ("Enter the url of the tender website you want scraped:")
limit = st.number_input("How many tenders do you want? ",min_value=1, step=1, format="%d")

## 1. scraping the data from the web
if st.button("scrape site"):
    st.write("scraping site....")
    tend_table = scrape_tenders(websites, limit)
    st.write("Scraping completed!")
## 2. save the tenders as a csv file
    save_tenders_to_csv(tend_table)
    st.write("Tenders saved in a csv file.")
    st.write("Click the send email button to receive the file in your email.")

    webites = ""
    limit = 1
## 4. send the tenders file as an email
if st.button("Send Email"):
    send_email_with_csv(subject, from_email, password,to_email, body, csv_file_path, smtp_port=587, smtp_server="smtp.gmail.com")
    st.write("Check you email for the tenders!")

