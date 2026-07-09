import streamlit as st
import requests

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)

# =============================
# CSS
# =============================

st.markdown("""
<style>

.main{
    background:#F6F8FC;
}

.title{
    text-align:center;
    color:#003366;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
}

</style>
""",unsafe_allow_html=True)

# =============================
# HEADER
# =============================

st.markdown("<div class='title'>🩺 Breast Cancer Prediction</div>",unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Support Vector Machine (SVM)</div>",unsafe_allow_html=True)

st.markdown("---")

st.markdown("<div class='card'>",unsafe_allow_html=True)

st.subheader("Patient Information")

col1,col2,col3=st.columns(3)

inputs=[]

for i in range(30):

    if i%3==0:
        with col1:
            value=st.number_input(f"Feature {i+1}",0.0)
    elif i%3==1:
        with col2:
            value=st.number_input(f"Feature {i+1}",0.0)
    else:
        with col3:
            value=st.number_input(f"Feature {i+1}",0.0)

    inputs.append(value)

st.markdown("</div>",unsafe_allow_html=True)

st.write("")

colA,colB,colC=st.columns([2,1,2])

with colB:
    predict=st.button("🔍 Predict",use_container_width=True)

if predict:

    url="https://svm-fastapi-streamlit-production-3f17.up.railway.app/predict"

    with st.spinner("Predicting..."):

        try:

            response=requests.post(
                url,
                json={"features":inputs},
                timeout=30
            )

                        hasil = response.json()

            st.markdown("---")

            prob = hasil["probability"] * 100

            if hasil["prediction"] == 1:

                warna = "#ffebee"
                border = "#e53935"
                status = "🔴 MALIGNANT"
                risk = "HIGH RISK"
                pesan = "Segera konsultasikan hasil ini kepada tenaga medis untuk pemeriksaan lebih lanjut."

            else:

                warna = "#e8f5e9"
                border = "#43a047"
                status = "🟢 BENIGN"
                risk = "LOW RISK"
                pesan = "Kemungkinan termasuk kategori Benign. Tetap lakukan pemeriksaan kesehatan secara berkala."

            st.markdown(f"""
            <div style="
            background:{warna};
            padding:30px;
            border-radius:20px;
            border-left:10px solid {border};
            box-shadow:0px 6px 15px rgba(0,0,0,0.2);
            ">

            <h1 style="text-align:center;color:{border};">
            {status}
            </h1>

            </div>
            """, unsafe_allow_html=True)

            st.write("")

            col1,col2,col3=st.columns(3)

            with col1:
                st.metric("Prediction", status)

            with col2:
                st.metric("Probability", f"{prob:.2f}%")

            with col3:
                st.metric("Risk Level", risk)

            st.write("")

            st.progress(prob/100)

            st.info(pesan)

        except Exception as e:

            st.error(e)
