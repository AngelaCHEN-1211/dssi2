import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
apptitle = 'DSSI Iris App'

st.set_page_config(page_title=apptitle, layout='wide')

st.title('Workshop Streamlit Application')
st.write('Reference: https://docs.streamlit.io/en/stable/api.html#display-data')
st.balloons() 

# Load diabetes dataset
st.subheader('**Iris Data**')
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

col1, col2 = st.columns([2,1])
with col1:
    # Display dataframe as an interactive table
    st.dataframe(df, use_container_width=True)
with col2:
    # Plot histogram for iris feature (sepal length)
    fig, ax = plt.subplots(figsize=(6, 3))
    if True:
        # 把 age 改成 iris 的特征：sepal length (cm)
        df['sepal length (cm)'].hist(bins = 10, ax=ax)
        fig.suptitle("Sepal Length Distribution")
        st.pyplot(fig)
