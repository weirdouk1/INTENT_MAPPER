import asyncio
from services.logger import log_event

async def async_log(data):
  await asyncio.sleep(0)
  log_event(data)