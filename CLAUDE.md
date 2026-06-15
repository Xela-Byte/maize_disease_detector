# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

There are no tests or linters configured.

## Secrets Required

Before running locally, populate `.streamlit/secrets.toml` (never commit this file):

```toml
MODEL_FILE_ID  = "<google-drive-file-id-for-maize_cnn_final.keras>"
LABELS_FILE_ID = "<google-drive-file-id-for-class_labels.json>"
```

The model (`maize_cnn_final.keras`) and label map (`class_labels.json`) must be publicly shared on Google Drive. On first run, `model_loader.py` downloads them to `/tmp` and caches them for the lifetime of the Streamlit process via `@st.cache_resource`.

## Architecture

The app is a single-page Streamlit interface (`app.py`) that wires together three utility modules:

| Module | Responsibility |
|--------|---------------|
| `utils/model_loader.py` | Downloads model + label JSON from Google Drive into `/tmp`, loads Keras model, returns `(model, idx_to_class)` |
| `utils/predictor.py` | Resizes PIL image to 128×128, normalises to `[0, 1]`, runs a forward pass, returns `(pred_class, confidence, all_preds)` |
| `utils/disease_info.py` | Pure-data dict `DISEASE_INFO` keyed by class name — holds description, symptoms, treatment list, severity, and UI colours per disease |

**Data flow:** `app.py` calls `load_model_and_labels()` at startup → user uploads image → `predict()` runs inference → `DISEASE_INFO[pred_class]` drives the result UI (confidence bar chart via Plotly, symptoms, treatment cards).

**Four output classes:** `Common_Rust`, `Gray_Leaf_Spot`, `Northern_Leaf_Blight`, `Healthy`. Class names are loaded at runtime from the JSON label map (integer index → class name), so `DISEASE_INFO` keys must stay in sync with that map.

## Deployment

Deployed on Streamlit Cloud. Secrets are configured via **App Settings → Secrets** (not committed). The `/tmp` cache does not persist across Streamlit Cloud restarts, so the Drive download runs once per cold start.
