from sentence_transformers import CrossEncoder

from config import CROSS_MODEL


model = CrossEncoder(CROSS_MODEL)



def rerank(query, candidates):

  pairs = [
    (query, c["text"])
    for c in candidates
  ]

  scores = model.predict(pairs)

  results = []

  for item, ce_score in zip(candidates, scores):

    results.append({
      "intent": item["intent"],
      "text": item["text"],
      "semantic_score": item["semantic_score"],
      "ce_score": float(ce_score)
    })

  ranked = sorted(
    results,
    key=lambda x: x["ce_score"],
    reverse=True
  )

  return ranked