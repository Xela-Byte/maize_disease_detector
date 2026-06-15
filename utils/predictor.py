"""
Inference helper.

Takes a PIL image, preprocesses it to match training conditions
(128×128, normalised to [0, 1]), and returns the predicted class,
confidence score, and the full probability array.
"""

import numpy as np
from PIL import Image

IMG_SIZE   = (128, 128)
NUM_CLASSES = 4


def predict(image: Image.Image, model, idx_to_class: dict) -> tuple:
    """
    Run a single-image forward pass through the CNN.

    Args:
        image:        PIL Image (any size / mode — will be resized & normalised).
        model:        Loaded Keras model.
        idx_to_class: Mapping from integer index → class name string.

    Returns:
        (pred_class, confidence, all_preds)
        - pred_class  : str   — winning class name, e.g. "Common_Rust"
        - confidence  : float — probability of winning class × 100 (percentage)
        - all_preds   : np.ndarray shape (NUM_CLASSES,) — full softmax output
    """
    img       = image.resize(IMG_SIZE)
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)        # (1, 128, 128, 3)

    preds      = model.predict(img_array, verbose=0)[0]  # (NUM_CLASSES,)
    pred_idx   = int(np.argmax(preds))
    pred_class = idx_to_class[pred_idx]
    confidence = float(np.max(preds)) * 100.0

    return pred_class, confidence, preds
