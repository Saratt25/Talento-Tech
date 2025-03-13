chart_data = pd.DataFrame(
    np.random.randn(20,3),   #Genero valores aleatorios
    columns=["a", "b", "c"]) #Genero las columnas
st.write(chart_data)     #Crear lineas interactivas
st.line_chart(chart_data)

import pandas as pd
import numpy as np
import matplotlib as pt
import seaborn as sns

import streamlit as st
st.write("Hello world")