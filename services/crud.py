from services.storage import INTENT_DB
from services.intent import rebuild_domain
from services.cache import invalidate


def add_intent(domain, intent):
  INTENT_DB.setdefault(domain, []).append(intent)
  rebuild_domain(domain)
  invalidate()


def remove_intent(domain, intent):
  if intent in INTENT_DB.get(domain, []):
    INTENT_DB[domain].remove(intent)
    rebuild_domain(domain)
    invalidate()


def update_intent(domain, old, new):
  remove_intent(domain, old)
  add_intent(domain, new)