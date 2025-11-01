import streamlit as st
from pages.home import home_page
from pages.register import register_page
from pages.login import login_page
from pages.upload import upload_page
from pages.jobs import jobs_page
from pages.scheduler import scheduler_page
from pages.dashboard import dashboard_page
from utils.db import init_db, get_conn

st.set_page_config(page_title="AI Recruitment System", layout="wide")
init_db()

menu = st.sidebar.selectbox("Navigation", ["Home","Register","Login","Upload Resume","Jobs","Scheduler","Dashboard"])

if menu == "Home":
    home_page()
elif menu == "Register":
    register_page()
elif menu == "Login":
    login_page()
elif menu == "Upload Resume":
    upload_page()
elif menu == "Jobs":
    jobs_page()
elif menu == "Scheduler":
    scheduler_page()
elif menu == "Dashboard":
    dashboard_page()
