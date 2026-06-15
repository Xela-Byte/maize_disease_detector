"""
Disease metadata: descriptions, symptoms, treatment recommendations,
severity levels and UI display properties for each maize disease class.
"""

DISEASE_INFO = {
    "Common_Rust": {
        "description": (
            "Common Rust is caused by the fungus Puccinia sorghi. It appears as small, "
            "oval to elongated, golden-brown pustules scattered on both leaf surfaces. "
            "It thrives in cool, moist conditions and can spread rapidly across a field."
        ),
        "symptoms": (
            "Small circular to elongated cinnamon-brown pustules on both leaf surfaces. "
            "Leaves may turn yellow and dry out in severe cases."
        ),
        "treatment": [
            "Apply fungicides containing Mancozeb or Azoxystrobin early",
            "Plant resistant maize hybrid varieties",
            "Ensure proper field drainage to reduce moisture",
            "Remove and destroy infected plant debris after harvest",
            "Apply fungicide spray every 7–14 days during humid conditions",
            "Scout fields weekly during the growing season",
        ],
        "severity": "Moderate",
        "color":    "#c0692a",
        "bg_color": "#fdf0e8",
        "icon":     "🟠",
    },
    "Gray_Leaf_Spot": {
        "description": (
            "Gray Leaf Spot is caused by the fungus Cercospora zeae-maydis. "
            "It is one of the most significant yield-limiting diseases of maize worldwide, "
            "thriving in warm, humid conditions with heavy dew."
        ),
        "symptoms": (
            "Rectangular, tan to gray lesions with distinct parallel edges running between "
            "leaf veins. Lesions turn gray as they mature and may merge to kill entire leaves."
        ),
        "treatment": [
            "Apply fungicides containing Pyraclostrobin or Propiconazole",
            "Use certified disease-resistant seed varieties",
            "Practice crop rotation with non-host crops (soybean, wheat)",
            "Improve air circulation by reducing plant density",
            "Avoid overhead irrigation to reduce leaf wetness duration",
            "Till crop residue to reduce fungal inoculum in soil",
        ],
        "severity": "High",
        "color":    "#5d6d6e",
        "bg_color": "#f0f2f2",
        "icon":     "⬜",
    },
    "Healthy": {
        "description": (
            "The maize leaf appears healthy with no signs of disease, pest damage, "
            "or nutrient deficiency. Continue current management practices to maintain "
            "crop health throughout the growing season."
        ),
        "symptoms": (
            "No disease symptoms detected. The leaf shows normal green coloration, "
            "healthy tissue structure, and no lesions or pustules."
        ),
        "treatment": [
            "Continue current crop management practices",
            "Maintain regular field scouting every 7 days",
            "Ensure adequate and balanced fertilization (NPK)",
            "Maintain proper irrigation schedule",
            "Monitor for early signs of pest or disease pressure",
            "Keep field records for future crop planning",
        ],
        "severity": "None",
        "color":    "#2d7a1b",
        "bg_color": "#f0f7e8",
        "icon":     "✅",
    },
    "Northern_Leaf_Blight": {
        "description": (
            "Northern Leaf Blight is caused by the fungus Exserohilum turcicum. "
            "It is a serious foliar disease that can cause 30–50% yield losses in "
            "susceptible varieties under favourable conditions."
        ),
        "symptoms": (
            "Long, elliptical, grayish-green to tan lesions (2.5–15 cm) that run "
            "parallel to leaf margins. Lesions have a distinctive cigar or canoe shape."
        ),
        "treatment": [
            "Apply fungicides containing Propiconazole or Tebuconazole",
            "Plant NLB-resistant hybrid varieties",
            "Practice crop rotation every 1–2 seasons",
            "Till soil deeply to bury infected debris after harvest",
            "Scout fields regularly and apply fungicide at first sign",
            "Avoid late planting which increases disease risk",
        ],
        "severity": "High",
        "color":    "#8b2500",
        "bg_color": "#fdf0ee",
        "icon":     "🔴",
    },
}
