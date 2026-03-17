import streamlit as st
import pandas as pd

data = pd.read_csv("titanic.csv")

page_1 = st.Page("survival_rate.py",title="Survival Rate",icon=":material/analytics:")
page_2 = st.Page("columns_relationship.py",title="Columns Relationship",icon=":material/dashboard_2_gear:")
page_3 = st.Page("ship_map_analysis.py",title="Ship Map Analysis",icon=":material/directions_boat:")
page_4 = st.Page("would_you_survive.py",title="Would You Survive",icon=":material/person_raised_hand:")

pg = st.navigation([page_1,page_2,page_3,page_4])
pg.run()