from config import (
  CONF_THRESHOLD,
  MARGIN_THRESHOLD,
  LAMBDA
)

from services.cross_encoder import rerank



def decide(query, ranked):

  if not ranked:
    return "out_of_scope", []

  top_item = ranked[0]

  top_intent = top_item["intent"]
  top_score = top_item["final_score"]


  if top_score >= CONF_THRESHOLD:
    return top_intent, ranked


  if len(ranked) > 1:

    second_score = ranked[1]["final_score"]

    if abs(top_score - second_score) < MARGIN_THRESHOLD:

      ce_candidates = ranked[:5]

      ce_ranked = rerank(query, ce_candidates)

      fused = []

      for item in ce_ranked:

        semantic = item["semantic_score"]
        ce = item["ce_score"]

        final_score = (
          (LAMBDA["semantic"] * semantic)
          +
          (LAMBDA["ce"] * ce)
        )

        fused.append({
          "intent": item["intent"],
          "text": item["text"],
          "semantic_score": semantic,
          "ce_score": ce,
          "final_score": final_score
        })

      fused = sorted(
        fused,
        key=lambda x: x["final_score"],
        reverse=True
      )

      return fused[0]["intent"], fused


  return top_intent, ranked