import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
st.title("""LOAN DATASET""")
df=pd.read_csv("loan_data.csv")
st.write(df)
df.dropna(inplace=True)
fig=plt.figure()
st.title("""UNIVARIATE VISUALIZATION""")
sns.histplot(df['ownership'])
st.pyplot(fig)
fig=plt.figure()
sns.histplot(df['default'])
st.pyplot(fig)
fig=plt.figure()
st.title("""Plot between interest and amount""")

st.pyplot(sns.jointplot(x=df['interest'],y=df['income'],kind="reg"))
st.pyplot(sns.pairplot(df[['interest','income','amount']]))
fig=plt.figure()
st.title("""Plot between amount,default,ownership""")
sns.barplot(x=df['default'],y=df['amount'],hue=df['ownership'])
st.pyplot(fig)
