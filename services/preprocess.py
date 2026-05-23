import re
import unicodedata


def normalize(q):

  q = unicodedata.normalize("NFKC", q)

  q = q.lower().strip()

  q = re.sub(r"[^a-z0-9\s]", " ", q)

  q = re.sub(r"\s+", " ", q)

  return q