def apply_context(q, ctx):
  if not ctx:
    return q, 0
  boost = 0.1 if ctx.get("domain") else 0
  return q + " " + " ".join(ctx.get("entities", [])), boost