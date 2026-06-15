import os
import json
import requests
import streamlit as st
from tensorflow import keras

_MODEL_CACHE  = "/tmp/maize_cnn_final.keras"
_LABELS_CACHE = "/tmp/class_labels.json"

_BASE_DIR         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_LOCAL_MODEL      = os.path.join(_BASE_DIR, "data", "maize_cnn_final.keras")
_LOCAL_LABELS     = os.path.join(_BASE_DIR, "data", "class_labels.json")


def _download_from_gdrive(file_id: str, dest: str) -> None:
    session  = requests.Session()
    url      = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = session.get(url, stream=True)
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            url      = f"{url}&confirm={value}"
            response = session.get(url, stream=True)
            break
    with open(dest, "wb") as fh:
        for chunk in response.iter_content(chunk_size=32_768):
            if chunk:
                fh.write(chunk)


@st.cache_resource(show_spinner=False)
def load_model_and_labels():
    # Model: local file → /tmp cache → Google Drive
    if os.path.exists(_LOCAL_MODEL):
        model_src = _LOCAL_MODEL
    else:
        if not os.path.exists(_MODEL_CACHE):
            with st.spinner("Downloading model — one-time setup…"):
                _download_from_gdrive(st.secrets["MODEL_FILE_ID"], _MODEL_CACHE)
        model_src = _MODEL_CACHE

    # Labels: same priority order
    if os.path.exists(_LOCAL_LABELS):
        labels_src = _LOCAL_LABELS
    else:
        if not os.path.exists(_LABELS_CACHE):
            with st.spinner("Downloading class labels…"):
                _download_from_gdrive(st.secrets["LABELS_FILE_ID"], _LABELS_CACHE)
        labels_src = _LABELS_CACHE

    model = keras.models.load_model(model_src)
    with open(labels_src) as fh:
        class_indices = json.load(fh)
    return model, {v: k for k, v in class_indices.items()}
