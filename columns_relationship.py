import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from navigation import data

st.title("Columns Relationship")


corr_columns_1 = st.multiselect("select rows",options=["survived","pclass","age","sibsp","parch","fare"],default=["survived","age"])


fix, ax = plt.subplots()
sns.heatmap(data=data.loc[:,corr_columns_1].corr(),annot=True)
st.write(fix)
