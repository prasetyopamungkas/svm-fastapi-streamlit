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

            hasil=response.json()

            st.markdown("---")

            if hasil["prediction"]==1:

                st.error("## 🔴 Malignant")

            else:

                st.success("## 🟢 Benign")

            st.metric(
                "Prediction Probability",
                f"{hasil['probability']:.2%}"
            )

        except Exception as e:

            st.error(e)
