import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def cstr_volume(k, F_A0, X):
    #Calculates the volume of a CSTR for a first-order reaction.
    return F_A0 * X / (k * (1 - X))

def pfr_volume(k, F_A0, X):
    #Calculates the volume of a PFR for a first-order reaction.
    return (F_A0 / k) * np.log(1 / (1 - X))

def pfr_conversion_profile(k, F_A0):
    #Calculates the conversion profile along a PFR.
    X = np.linspace(0, 1, 100)
    V_pfr = np.zeros_like(X)
    for i in range(len(X)):
        V_pfr[i] = pfr_volume(k, F_A0, X[i])
    return X, V_pfr


st.title("CSTR and PFR Calculator")

# Input parameters
k = st.number_input("Reaction rate constant (k)", value=1.0, min_value=0.1, max_value=5.0, step=0.1)
F_A0 = st.number_input("Feed rate (F_A0)", value=1.0, min_value=0.0, max_value=5.0, step=0.1)
X = st.number_input("Target conversion (X)", value=0.9, min_value=0.0, max_value=1.0, step=0.05)

# Calculate reactor volumes
V_cstr = cstr_volume(k, F_A0, X)
V_pfr = pfr_volume(k, F_A0, X)

# Display results
st.write("CSTR Volume:", V_cstr)
st.write("PFR Volume:", V_pfr)

# Plot conversion profiles

st.header("PFR Conversion")
X_pfr, V_PFR = pfr_conversion_profile(k, F_A0)
fig, ax = plt.subplots()
ax.plot(X_pfr, V_PFR, label="Conversion Profile", color='blue')
ax.set_xlabel("Conversion")
ax.set_ylabel("Volume of PFR")
ax.set_title("PFR Conversion Rate")

st.pyplot(fig)
