import pandas as pd
import numpy as np
import matplotlib as pt
import seaborn as sns

import streamlit as st
st.write("Hello world")

dataframe = pd.DataFrame(
    np.random.randn(10,20),   #Creamos valores aleatorios
    columns=("col %d" % i for i in range(20)))
#Aplicamos estilo "highlight" a DataFrame
st.dataframe(dataframe.style.highlight_max(axis=0))
