from config import LAMBDA



def compute_scores(retrieved):

  results = []

  for item in retrieved:

    semantic_score = item["semantic_score"]

    final_score = (
      LAMBDA["semantic"] * semantic_score
    )

    results.append({
      "intent": item["intent"],
      "text": item["text"],
      "semantic_score": semantic_score,
      "final_score": final_score
    })

  ranked = sorted(
    results,
    key=lambda x: x["final_score"],
    reverse=True
  )

  return ranked