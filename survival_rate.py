import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from navigation import data
st.title("Survival Rate",text_alignment="center")

col = st.columns([3,1])
count = col[0].slider("Percentage of data ",min_value=0,max_value=100, value=70)
df_filter = col[1].selectbox("Filter",options=("pclass","sex","sibsp","embarked","class","who","deck")) 
filtered_range = round(len(data)*(count/100))
cool = col[1].columns(2)




fix, ax = plt.subplots()
sns.barplot(data=data.iloc[0:filtered_range],x=df_filter,  y="survived",ax=ax,hue=df_filter,legend=False,errorbar=None)
for container in ax.containers:
    ax.bar_label(container,fmt="%.2f")
st.write(fix)