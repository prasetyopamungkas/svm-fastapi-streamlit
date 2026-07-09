import streamlit as st
import requests

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🩺 SVM Prediction")

st.sidebar.markdown("""
### Breast Cancer Prediction

Aplikasi ini menggunakan model
**Support Vector Machine (SVM)** untuk
memprediksi apakah data termasuk:

- 🟢 Benign
- 🔴 Malignant

Masukkan nilai 30 fitur kemudian tekan tombol **Predict**.
""")

# ==========================
# HEADER
# ==========================

st.title("🩺 Breast Cancer Prediction")

st.markdown("---")

st.write("### Input Feature")

# ==========================
# INPUT
# ==========================

inputs = []

col1, col2 = st.columns(2)

with st.form("prediction_form"):

    for i in range(15):
        with col1:
            value = st.number_input(
                f"Feature {i+1}",
                value=0.0,
                format="%.4f"
            )
            inputs.append(value)

    for i in range(15,30):
        with col2:
            value = st.number_input(
                f"Feature {i+1}",
                value=0.0,
                format="%.4f"
            )
            inputs.append(value)

    submitted = st.form_submit_button("🔍 Predict")

# ==========================
# PREDICT
# ==========================

if submitted:

    API_URL = "https://svm-fastapi-streamlit-production-3f17.up.railway.app/predict"

    with st.spinner("Predicting..."):

        try:

            response = requests.post(
                API_URL,
                json={"features": inputs},
                timeout=30
            )

            hasil = response.json()

            if response.status_code == 200:

                st.markdown("---")

                c1,c2 = st.columns(2)

                with c1:

                    if hasil["prediction"] == 1:
                        st.error("🔴 Prediction : Malignant")
                    else:
                        st.success("🟢 Prediction : Benign")

                with c2:

                    st.metric(
                        "Probability",
                        f"{hasil['probability']:.2%}"
                    )

            else:

                st.error("API Error")
                st.json(hasil)

        except Exception as e:

            st.error("Tidak dapat terhubung ke FastAPI")
            st.exception(e)
