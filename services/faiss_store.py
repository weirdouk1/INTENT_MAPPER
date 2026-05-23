import faiss
import numpy as np

class FaissStore:
  def __init__(self, dim=384):
    self.index = faiss.IndexFlatIP(dim)
    self.labels = []

  def add(self, vecs, labels):
    if len(vecs) == 0: return
    self.index.add(np.array(vecs).astype('float32'))
    self.labels.extend(labels)

  def reset(self):
    self.index.reset(); self.labels = []

  def search(self, q_vec, k=5):
    if len(self.labels) == 0: return []
    D, I = self.index.search(np.array([q_vec]).astype('float32'), k)
    return [(self.labels[i], D[0][idx]) for idx, i in enumerate(I[0]) if i < len(self.labels)]
