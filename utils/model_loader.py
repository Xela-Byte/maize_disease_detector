import os
import json
import streamlit as st
import keras

_BASE_DIR     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MODEL_PATH   = os.path.join(_BASE_DIR, "data", "maize_cnn_final.keras")
_LABELS_PATH  = os.path.join(_BASE_DIR, "data", "class_labels.json")


@st.cache_resource(show_spinner=False)
def load_model_and_labels():
    model = keras.models.load_model(_MODEL_PATH)
    with open(_LABELS_PATH) as fh:
        class_indices = json.load(fh)
    return model, {v: k for k, v in class_indices.items()}
