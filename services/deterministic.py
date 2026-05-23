def match(q):
  if "password" in q and "reset" in q:
    return ("auth", "reset_password")
  return None