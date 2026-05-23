def update_weights(w, reward, pred, feat, lr=0.01):
  return w + lr * (reward - pred) * feat