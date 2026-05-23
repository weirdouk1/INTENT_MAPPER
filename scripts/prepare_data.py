from datasets import load_dataset
import pandas as pd
import os
import re

from sklearn.model_selection import (
  train_test_split
)

print("Loading dataset...")

ds = load_dataset(
  "clinc_oos",
  "plus"
)

print("Dataset loaded!")

os.makedirs(
  "data/processed",
  exist_ok=True
)

intent_names = (
  ds["train"]
  .features["intent"]
  .names
)


def clean(q):

  q = str(q)

  q = q.lower().strip()

  q = q.replace('"', '')

  q = re.sub(
    r"[^a-z0-9\s]",
    " ",
    q
  )

  q = re.sub(
    r"\s+",
    " ",
    q
  )

  return q


def convert_all():

  rows = []

  for split in [
    "train",
    "validation",
    "test"
  ]:

    for item in ds[split]:

      query = clean(
        item["text"]
      )

      intent = intent_names[
        item["intent"]
      ]

      if intent == "oos":
        intent = "out_of_scope"

      rows.append({
        "query": query,
        "intent": intent
      })

  df = pd.DataFrame(rows)

  df = df.sample(
    frac=1,
    random_state=42
  ).reset_index(drop=True)

  return df


print("Preparing dataset...")

df = convert_all()

print("Total samples:", len(df))


train_df, temp_df = train_test_split(
  df,
  test_size=0.3,
  stratify=df["intent"],
  random_state=42
)

val_df, test_df = train_test_split(
  temp_df,
  test_size=0.5,
  stratify=temp_df["intent"],
  random_state=42
)


train_df.to_csv(
  "data/processed/train.csv",
  index=False
)

val_df.to_csv(
  "data/processed/val.csv",
  index=False
)

test_df.to_csv(
  "data/processed/test.csv",
  index=False
)

print()

print("Data prepared successfully!")

print()

print("Train:", len(train_df))
print("Validation:", len(val_df))
print("Test:", len(test_df))

print()

print("Intent distribution:")

print(
  train_df["intent"]
  .value_counts()
  .head()
)