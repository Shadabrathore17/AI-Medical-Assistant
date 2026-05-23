import pandas as pd
import random

# Diseases
diseases = [

    "Fever",
    "Headache",
    "Cold",
    "Cough",
    "Diabetes",
    "BP",
    "Acidity",
    "Asthma",
    "Typhoid",
    "Migraine",
    "Allergy",
    "Skin Infection",
    "Joint Pain",
    "Tooth Pain",
    "Ear Infection",
    "Eye Infection",
    "Stomach Pain",
    "Vomiting",
    "Diarrhea",
    "Weakness"
]

# Medicines
medicines = [

    "Paracetamol",
    "Ibuprofen",
    "Cetirizine",
    "Azithromycin",
    "Metformin",
    "Amlodipine",
    "Antacid",
    "Salbutamol Inhaler",
    "ORS",
    "Cough Syrup",
    "Vitamin Tablets",
    "Pain Relief Gel",
    "Antibiotic Cream",
    "Calcium Tablets",
    "Insulin",
    "Omeprazole",
    "Dolo 650",
    "Crocin",
    "Pantoprazole",
    "Amoxicillin"
]

# Usage
usages = [

    "Take after meal",
    "Take before meal",
    "Use twice daily",
    "Use once daily",
    "Take before sleep",
    "Drink water with medicine"
]

# Symptoms
symptoms = [

    "Body pain and weakness",
    "Sneezing and cough",
    "High temperature",
    "Breathing problem",
    "Burning sensation",
    "Head pain and stress",
    "Vomiting and nausea",
    "Stomach infection"
]

# Precautions
precautions = [

    "Avoid spicy food",
    "Take proper rest",
    "Drink warm water",
    "Avoid cold drinks",
    "Do not overdose",
    "Consult doctor if problem continues"
]

# Side Effects
side_effects = [

    "Sleepiness",
    "Dizziness",
    "Nausea",
    "Dry mouth",
    "Fatigue",
    "Constipation"
]

# Create Rows
rows = []

for i in range(1100):

    row = {

        "Disease": random.choice(diseases),

        "Medicine": random.choice(medicines),

        "Usage": random.choice(usages),

        "Symptoms": random.choice(symptoms),

        "Precautions": random.choice(precautions),

        "SideEffects": random.choice(side_effects)
    }

    rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows)

# Save CSV
df.to_csv(

    "medicines.csv",

    index=False
)

print("Dataset Created Successfully")
print("File Name: medicines.csv")