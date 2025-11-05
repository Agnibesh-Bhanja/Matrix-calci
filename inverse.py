import streamlit as st
import numpy as np

st.set_page_config(page_title="ankara_messi_calci", page_icon="🔢", layout="centered")

st.markdown(
    "<h1 style='font-family:Courier New; color:white;font-size:50px;'>🔢Matrix Calculator</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='font-family:Courier New;color:#FF6600; font-size:40px;'>Inverse of matrix</h3>",
    unsafe_allow_html=True
)

st.write("<h6 style='font-family:Courier New;color:#FF6600; font-size:15px;'>Enter the elements of your 3×3 matrix below (row-wise):</h6>",
    unsafe_allow_html=True)

A = []
for i in range(3):
    cols = st.columns(3)
    row = []
    for j in range(3):
        val = cols[j].number_input(f"a{i+1}{j+1}", value=0.0, key=f"cell_{i}_{j}")# key=f is unique key statements
        row.append(val)
    A.append(row)

# Button 
if st.button("Inverse boom"):
    tot = []
    for i in range(3):
        tot.append(A[i] + [1 if i == j else 0 for j in range(3)])

    try:
        for i in range(3):
            dia = tot[i][i]
            if dia == 0:
                st.error("❌ Matrix is singular — inverse does not exist.")
                st.stop()

            for j in range(6):
                tot[i][j] /= dia

            for k in range(3):
                if k != i:
                    factor = tot[k][i]
                    for j in range(6):
                        tot[k][j] -= factor * tot[i][j]

        inverse = [row[3:] for row in tot]

        st.success("✅ Inverse Matrix:")
        st.table(np.round(inverse, 2))

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

st.markdown(
    "<h3 style='font-family:Courier New;color:#FF6600; font-size:40px;'>Eigen values</h3>",
    unsafe_allow_html=True
)


st.markdown("---")
st.caption("Built by Agnibesh")
