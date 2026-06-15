# 🌽 Maize Disease Detection System

An AI-powered Streamlit web app that diagnoses maize leaf diseases from photos using a custom CNN trained on the PlantVillage dataset.

**Detectable diseases:** Common Rust · Gray Leaf Spot · Northern Leaf Blight · Healthy

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 95.51% |
| Precision | 95.83% |
| Recall    | 95.34% |
| F1-Score  | 95.58% |

---

## Project Structure

```
maize_disease_detector/
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── .gitignore
├── .streamlit/
│   ├── config.toml            # UI theme & server settings
│   └── secrets.toml           # 🔒 NOT committed — holds Drive file IDs
└── utils/
    ├── __init__.py
    ├── disease_info.py        # Disease descriptions, symptoms, treatments
    ├── model_loader.py        # Downloads model from Drive + caches it
    └── predictor.py           # Image preprocessing + CNN inference
```

---

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/maize-disease-detection.git
cd maize-disease-detection

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your secrets (see below)
# Edit .streamlit/secrets.toml with your real Google Drive file IDs

# 5. Run the app
streamlit run app.py
```

---

## Preparing Your Google Drive Files

Your trained model (`maize_cnn_final.keras`) and labels (`class_labels.json`)
must be publicly accessible on Google Drive.

### Step 1 — Make files public

1. Go to [drive.google.com](https://drive.google.com)
2. Right-click `maize_cnn_final.keras` → **Share**
3. Change access to **Anyone with the link → Viewer**
4. Copy the link — the file ID is the long string between `/d/` and `/view`:
   ```
   https://drive.google.com/file/d/XXXXXXXXXXXXXXXXXXXXXXX/view
                                   ↑ this is your FILE_ID
   ```
5. Repeat for `class_labels.json`

### Step 2 — Add IDs to secrets.toml

```toml
# .streamlit/secrets.toml
MODEL_FILE_ID  = "1TFh--_JBvZz5x2tHVAHGfarBFdwheozR"   # ← your model ID
LABELS_FILE_ID = "1g77IocRFwOLZywebPPBodrHom4jcIfd2"   # ← your labels ID
```

---

## Deploying to Streamlit Cloud (Free)

### Step 1 — Push code to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/maize-disease-detection.git
git push -u origin main
```

> ⚠️ Make sure `.streamlit/secrets.toml` is in `.gitignore` before pushing.

### Step 2 — Create a Streamlit Cloud account

Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.

### Step 3 — Deploy the app

1. Click **New app**
2. Select your repository: `YOUR_USERNAME/maize-disease-detection`
3. Branch: `main`
4. Main file path: `app.py`
5. Click **Deploy**

### Step 4 — Add secrets on Streamlit Cloud

1. Once deployed, click **⋮ → Settings → Secrets**
2. Paste this (with your real IDs):

```toml
MODEL_FILE_ID  = "your_model_file_id_here"
LABELS_FILE_ID = "your_labels_file_id_here"
```

3. Click **Save** — the app will automatically reboot with the secrets applied.

### Step 5 — Done!

Your app is live at:
```
https://YOUR_USERNAME-maize-disease-detection-app-XXXX.streamlit.app
```

---

## Tech Stack

- **Model:** Custom CNN (5 conv blocks, ~2.76M parameters) trained from scratch
- **Dataset:** PlantVillage via TensorFlow Datasets (3,852 maize images)
- **Framework:** TensorFlow 2.13 / Keras
- **App:** Streamlit 1.28
- **Charts:** Plotly

---

*Final Year Project — Computer Engineering*
