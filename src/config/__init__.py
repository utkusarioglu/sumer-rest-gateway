import os
import sys
import config.settings

APP_ENV = os.environ.get("APP_ENV", "Dev")
_current = getattr(
  sys.modules["config.settings"],
  f"{str.title(APP_ENV)}Config"
)()

for attr in [prop for prop in dir(_current) if not "__" in prop]:
  val = os.environ.get(attr, getattr(_current, attr))
  setattr(sys.modules[__name__], attr, val)

def as_dict():
  res = {}
  for attr in [prop for prop in dir(config) if not "__" in prop]:
    val = getattr(config, attr)
    res[attr] = val
  return res
