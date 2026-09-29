import pandas as pd

INPUT_FILE = "data/Artifacts.xlsm"
OUTPUT_FILE = "data/artifacts.csv"

# Load Excel data
df = pd.read_excel(INPUT_FILE, sheet_name="Sheet1")

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

# Rename existing columns
df = df.rename(columns={
    "Artifact ID Number": "artifact_id",
    "Artifact Name": "artifact_name",
    "Category": "category",
    "Brief Description": "description",
    "Material (if identiable)": "material",
    "Traditional Use/Purpose": "traditional_use",
    "Website Image/Reference": "image_reference",
    "Notes": "notes"
})

# Add fields needed by the cultural assistant
df["region_id"] = ""
df["tradition_id"] = ""
df["related_dance"] = ""
df["source_id"] = ""

# Put columns in our standard order
columns = [
    "artifact_id",
    "artifact_name",
    "category",
    "description",
    "material",
    "traditional_use",
    "region_id",
    "tradition_id",
    "related_dance",
    "image_reference",
    "source_id",
    "notes"
]

df = df[columns]

# Clean artifact IDs such as 1.0 -> 1
df["artifact_id"] = pd.to_numeric(
    df["artifact_id"], errors="coerce"
).astype("Int64")

# Save CSV
df.to_csv(OUTPUT_FILE, index=False)

print(f"Conversion complete.")
print(f"Artifacts exported: {len(df)}")
print(f"Saved to: {OUTPUT_FILE}")
