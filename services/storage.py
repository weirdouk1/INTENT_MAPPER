import pandas as pd
import os

file_path = "data/processed/train.csv"

if not os.path.exists(file_path):
  raise Exception("Run prepare_data.py first")

df = pd.read_csv(file_path)

INTENT_DB = {}

for _, row in df.iterrows():
  intent = row["intent"]
  query = row["query"]

  if intent not in INTENT_DB:
    INTENT_DB[intent] = []

  INTENT_DB[intent].append(query)