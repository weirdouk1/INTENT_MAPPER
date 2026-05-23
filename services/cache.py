import os
import redis

from dotenv import load_dotenv

from config import REDIS_TTL
from services.preprocess import normalize

load_dotenv()


r = redis.Redis(
  host=os.getenv("REDIS_HOST"),
  port=int(os.getenv("REDIS_PORT")),
  password=os.getenv("REDIS_PASSWORD"),
  ssl=True,
  decode_responses=True
)



def get(key):

  key = normalize(key)

  return r.get(key)



def set(key, val):

  key = normalize(key)

  r.set(
    key,
    val,
    ex=REDIS_TTL
  )



def invalidate(prefix="*"):

  for k in r.scan_iter(prefix):
    r.delete(k)