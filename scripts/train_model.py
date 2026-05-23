import json
import time

import pandas as pd

from datasets import Dataset

from setfit import (
  SetFitModel,
  Trainer,
  TrainingArguments
)

print("Loading processed CSV data...")


train_df = pd.read_csv(
  "data/processed/train.csv"
)

val_df = pd.read_csv(
  "data/processed/val.csv"
)


intent_names = sorted(
  train_df["intent"].unique()
)


label2id = {
  name: i
  for i, name in enumerate(intent_names)
}

id2label = {
  i: name
  for name, i in label2id.items()
}


def df_to_dataset(df):

  return Dataset.from_dict({
    "text": df["query"].tolist(),
    "label": [
      label2id[x]
      for x in df["intent"]
    ]
  })


train_data = df_to_dataset(
  train_df
)

val_data = df_to_dataset(
  val_df
)

print()

print("Training samples:",
      len(train_data))

print("Validation samples:",
      len(val_data))

print()

print("Loading model...")


model = SetFitModel.from_pretrained(
  "sentence-transformers/all-MiniLM-L6-v2"
)


args = TrainingArguments(

  batch_size=32,

  num_epochs=3,

  sampling_strategy="oversampling",

  num_iterations=5
)


trainer = Trainer(

  model=model,

  args=args,

  train_dataset=train_data,

  eval_dataset=val_data,

  metric="accuracy"
)


print()

print(
  "Training started at:",
  time.strftime("%H:%M:%S")
)

start = time.time()


trainer.train()


end = time.time()

print()

print(
  "Training ended at:",
  time.strftime("%H:%M:%S")
)

print(
  "Total training time:",
  round((end - start) / 60, 2),
  "minutes"
)

print()

print("Saving model...")


model.save_pretrained(
  "models/intent_model"
)


with open(
  "models/intent_model/label_map.json",
  "w"
) as f:

  json.dump(
    id2label,
    f
  )

print()

print("Training complete!")