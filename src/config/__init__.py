import os
import sys
import config.settings
from dotenv import dotenv_values

APP_ENV = os.environ.get("FLASK_ENV", "development")

_current = getattr(
  sys.modules["config.settings"],
  f"{str.title(APP_ENV)}Config"
)()

for attr in [prop for prop in dir(_current) if not "__" in prop]:
  val = os.environ.get(attr, getattr(_current, attr))
  setattr(sys.modules[__name__], attr, val)

def as_dict():
  res = dotenv_values()
  for attr in [prop for prop in dir(config) if not "__" in prop]:
    val = getattr(config, attr)
    res[attr] = val
  return res

def get(prop):
  return as_dict()[prop]
