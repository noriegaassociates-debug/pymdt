import streamlit as st
import numpy as np

st.title("GNES SDS + MIMO Dashboard")

v4 = st.number_input("V4 (simulation)", value=800.0)
v9 = st.number_input("V9 (sensor)", value=800.0)

KG = np.array([[ -0.5, 0.1],[0.1, -0.4]])
I = np.eye(2)
R = I + KG
sigma = np.min(np.linalg.svd(R, compute_uv=False))

SDS = 1 - abs(v4 - v9) / 850

st.metric("SDS", SDS)
st.metric("Sigma_min", sigma)

if SDS < 0.99 or sigma < 0.25:
    st.error("FAIL CLOSED")
else:
    st.success("SYSTEM STABLE")
