from pathlib import Path

import pandas as pd
import torch

from setfit import SetFitModel
from sentence_transformers import util

from config import (
  EMBED_MODEL,
  RETRIEVAL_POOL_MULTIPLIER
)


BASE_DIR = Path(__file__).resolve().parent.parent


model = SetFitModel.from_pretrained(
  EMBED_MODEL
)

embed_model = model.model_body


train_path = (
  BASE_DIR
  / "data"
  / "processed"
  / "train.csv"
)


df = pd.read_csv(train_path)

texts = df["query"].tolist()
labels = df["intent"].tolist()


embeddings = embed_model.encode(
  texts,
  convert_to_tensor=True,
  show_progress_bar=False
)



def retrieve_intents(query, k=10):

  q_vec = embed_model.encode(
    query,
    convert_to_tensor=True
  )

  scores = util.cos_sim(
    q_vec,
    embeddings
  )[0]

  retrieve_size = min(
    len(scores),
    max(
      k * RETRIEVAL_POOL_MULTIPLIER,
      k
    )
  )

  top_k = torch.topk(
    scores,
    k=retrieve_size
  )

  seen = set()

  results = []

  for idx in top_k.indices:

    idx = int(idx)

    intent = labels[idx]

    if intent in seen:
      continue

    seen.add(intent)

    results.append({
      "intent": intent,
      "semantic_score": float(scores[idx]),
      "text": texts[idx]
    })

    if len(results) >= k:
      break

  return results