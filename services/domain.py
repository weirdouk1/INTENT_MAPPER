from sentence_transformers import SentenceTransformer
from services.faiss_store import FaissStore

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed(x):
  return model.encode(x)


domain_store = None


def build_domain_store():
  global domain_store

  from services.storage import INTENT_DB   # 🔥 lazy import

  domains = list(INTENT_DB.keys())

  domain_store = FaissStore()

  if domains:
    domain_store.add(embed(domains), domains)


# build once at startup
build_domain_store()


def retrieve_domains(q_vec, k=2):
  return domain_store.search(q_vec, k)