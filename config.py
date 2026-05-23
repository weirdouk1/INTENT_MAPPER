import os

from dotenv import load_dotenv

load_dotenv()


EMBED_MODEL = os.getenv(
  "EMBED_MODEL",
  "models/intent_model"
)

CROSS_MODEL = os.getenv(
  "CROSS_MODEL",
  "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


REDIS_TTL = 3600


CONF_THRESHOLD = 0.55
MARGIN_THRESHOLD = 0.05

TOP_K_RETRIEVE = 5

RETRIEVAL_POOL_MULTIPLIER = 5


LAMBDA = {
  "semantic": 0.6,
  "ce": 0.4
}