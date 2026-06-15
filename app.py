import streamlit as st
import plotly.graph_objects as go
from PIL import Image

from utils.disease_info import DISEASE_INFO
from utils.model_loader import load_model_and_labels
from utils.predictor import predict

st.set_page_config(
    page_title="Maize Disease Detector",
    page_icon="🌽",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background-color: #f5f0e8; }
    .main-header {
        background: linear-gradient(135deg, #2d5a1b, #4a7c2f, #6b9e3f);
        padding: 2rem; border-radius: 15px; text-align: center;
        margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .main-header h1 { color: #f5f0e8; font-size: 2.5rem; font-weight: 800; margin: 0; }
    .main-header p  { color: #d4e8c2; font-size: 1.1rem; margin: 0.5rem 0 0 0; }
    .section-title {
        color: #2d5a1b; font-size: 1.3rem; font-weight: 700;
        border-bottom: 2px solid #8b6914; padding-bottom: 0.3rem;
        margin-bottom: 1rem;
    }
    .treatment-item {
        background: #f0f7e8; border-left: 4px solid #4a7c2f;
        padding: 0.6rem 1rem; margin: 0.4rem 0;
        border-radius: 0 8px 8px 0; color: #2d3a1b;
    }
    .metric-box {
        background: #2d5a1b; padding: 1rem;
        border-radius: 10px; text-align: center; margin: 0.3rem;
    }
    .metric-box h3 { color: #a8d878 !important; font-size: 1.8rem; margin: 0; }
    .metric-box p  { color: #d4e8c2 !important; font-size: 0.85rem; margin: 0; }
    .footer {
        background: #2d5a1b; color: #d4e8c2; text-align: center;
        padding: 1rem; border-radius: 10px; margin-top: 2rem; font-size: 0.85rem;
    }
    [data-testid="stSidebar"] { background-color: #2d5a1b !important; }
    [data-testid="stSidebar"] * { color: #f5f0e8 !important; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="main-header">
    <h1>🌽 Maize Disease Detection System</h1>
    <p>AI-powered crop disease diagnosis using Convolutional Neural Networks</p>
</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("## 🌱 About This System")
    st.markdown("Custom CNN trained on the **PlantVillage** dataset to detect maize leaf diseases.")
    st.markdown("---")
    st.markdown("### 📊 Model Performance")
    st.markdown("""
| Metric    | Score  |
|-----------|--------|
| Accuracy  | 95.51% |
| Precision | 95.83% |
| Recall    | 95.34% |
| F1-Score  | 95.58% |
""")
    st.markdown("---")
    st.markdown("### 🌿 Detectable Diseases")
    st.markdown("- 🟠 Common Rust")
    st.markdown("- ⬜ Gray Leaf Spot")
    st.markdown("- 🔴 Northern Leaf Blight")
    st.markdown("- ✅ Healthy")
    st.markdown("---")
    st.markdown("### ℹ️ How To Use")
    st.markdown("1. Upload a maize leaf photo")
    st.markdown("2. Wait for AI analysis")
    st.markdown("3. View diagnosis & confidence")
    st.markdown("4. Follow treatment advice")
    st.markdown("---")
    st.markdown("**Final Year Project | Computer Engineering**")


with st.spinner("Loading AI model..."):
    model, idx_to_class = load_model_and_labels()


st.markdown('<p class="section-title">📤 Upload Maize Leaf Image</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
    help="Upload a clear, well-lit photo of a maize leaf"
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<p class="section-title">🖼️ Uploaded Image</p>', unsafe_allow_html=True)
        st.image(image, use_container_width=True, caption="Submitted for analysis")

    with col2:
        st.markdown('<p class="section-title">🔍 AI Diagnosis</p>', unsafe_allow_html=True)
        with st.spinner("Analyzing with CNN..."):
            pred_class, confidence, all_preds = predict(image, model, idx_to_class)

        info  = DISEASE_INFO[pred_class]
        color = info["color"]

        st.markdown(f"""
        <div style="background:{info['bg_color']}; border-left:6px solid {color};
                    padding:1.2rem; border-radius:10px; margin-bottom:1rem;">
            <div style="font-size:2rem;">{info['icon']}</div>
            <h2 style="color:{color}; margin:0.3rem 0;">{pred_class.replace('_', ' ')}</h2>
            <p style="font-size:1.1rem; margin:0.2rem 0;">
                Confidence: <b style="color:{color};">{confidence:.1f}%</b>
            </p>
            <p style="margin:0; color:#555;">Severity: <b>{info['severity']}</b></p>
        </div>
        """, unsafe_allow_html=True)

        classes    = [idx_to_class[i].replace("_", " ") for i in range(len(idx_to_class))]
        bar_colors = [color if idx_to_class[i] == pred_class else "#c8b89a" for i in range(len(idx_to_class))]
        fig = go.Figure(go.Bar(
            x=all_preds * 100,
            y=classes,
            orientation="h",
            marker_color=bar_colors,
            marker_line=dict(color="#5a3e1b", width=1),
            text=[f"{v:.1f}%" for v in all_preds * 100],
            textposition="outside"
        ))
        fig.update_layout(
            xaxis_title="Confidence (%)",
            xaxis_range=[0, 115],
            height=220,
            margin=dict(l=5, r=40, t=10, b=30),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="#faf6ee",
            xaxis=dict(gridcolor="#e0d5c0"),
            font=dict(color="#2d3a1b")
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown(
        f'<p class="section-title">🔬 About {pred_class.replace("_", " ")}</p>',
        unsafe_allow_html=True
    )
    st.markdown(f"""
    <div style="background:#fff; border-radius:12px; padding:1.2rem;
                box-shadow:0 2px 10px rgba(0,0,0,0.08); border-top:4px solid {color};">
        <p style="color:#3a3a2a; line-height:1.6; margin:0;">{info['description']}</p>
    </div>
    """, unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="large")
    with col3:
        st.markdown('<p class="section-title">🩺 Symptoms</p>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background:#fff8ee; border:1px solid #d4a843;
                    padding:1rem; border-radius:10px; color:#3a3a2a; line-height:1.6;">
            {info['symptoms']}
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown('<p class="section-title">💊 Treatment Recommendations</p>', unsafe_allow_html=True)
        for tip in info["treatment"]:
            st.markdown(f'<div class="treatment-item">{tip}</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        🌽 AI-Powered Maize Disease Detection System &nbsp;|&nbsp;
        Final Year Project &nbsp;|&nbsp; Computer Engineering
    </div>
    """, unsafe_allow_html=True)

else:
    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        ("95.51%", "Test Accuracy"),
        ("95.58%", "F1-Score"),
        ("3,852",  "Training Images"),
        ("4",      "Disease Classes"),
    ]
    for col, (val, label) in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(
                f'<div class="metric-box"><h3>{val}</h3><p>{label}</p></div>',
                unsafe_allow_html=True
            )
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👆 Upload a maize leaf image above to get started!")
