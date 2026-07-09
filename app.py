# ==========================
# HASIL PREDIKSI
# ==========================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<style>

.result-card{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}

.result-title{
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:#003366;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="result-card">', unsafe_allow_html=True)

st.markdown('<div class="result-title">Prediction Result</div>', unsafe_allow_html=True)

st.markdown("---")

col1,col2,col3=st.columns(3)

prob=hasil["probability"]*100

with col1:

    if hasil["prediction"]==1:

        st.markdown(
            """
            <h2 style='color:red;text-align:center;'>
            🔴 Malignant
            </h2>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <h2 style='color:green;text-align:center;'>
            🟢 Benign
            </h2>
            """,
            unsafe_allow_html=True
        )

with col2:

    st.metric(
        label="Probability",
        value=f"{prob:.2f}%"
    )

with col3:

    if hasil["prediction"]==1:

        st.metric(
            label="Risk Level",
            value="High"
        )

    else:

        st.metric(
            label="Risk Level",
            value="Low"
        )

st.progress(prob/100)

st.write("")

if hasil["prediction"]==1:

    st.warning(
        """
### ⚠ Recommendation

The prediction indicates **Malignant**.

Please consult a medical professional for further examination.
"""
    )

else:

    st.success(
        """
### ✅ Recommendation

The prediction indicates **Benign**.

Continue routine medical check-ups as recommended by healthcare professionals.
"""
    )

st.markdown("</div>", unsafe_allow_html=True)
