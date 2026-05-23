import time

from fastapi import FastAPI

from config import TOP_K_RETRIEVE

from services.cache import (
  get,
  set,
  r
)

from services.decision import decide
from services.intent import retrieve_intents
from services.preprocess import normalize
from services.scorer import compute_scores


print("Redis Ping:", r.ping())
print("HYBRID + CONDITIONAL CE PIPELINE RUNNING")


app = FastAPI()


@app.post("/predict")
def predict(query: str):

  start = time.time()


  cache = get(query)

  if cache:

    return {
      "cached": True,
      "intent": cache,
      "latency_ms": round(
        (time.time() - start) * 1000,
        2
      )
    }


  q = normalize(query)


  retrieved = retrieve_intents(
    q,
    k=TOP_K_RETRIEVE
  )


  ranked = compute_scores(retrieved)


  final_intent, final_ranked = decide(
    q,
    ranked
  )


  top_k = [
    item["intent"]
    for item in final_ranked[:3]
  ]


  set(query, final_intent)


  latency = (time.time() - start) * 1000


  return {
    "intent": final_intent,
    "top_k": top_k,
    "latency_ms": round(latency, 2)
  }
