import config
import logging
from flask import Flask
from api import crete_apis
from dotenv import dotenv_values

config = dotenv_values(".env")

logging.basicConfig(
  level=logging.DEBUG,
  datefmt="%Y-%m-%d %H:%M:%S",
  handlers=[logging.StreamHandler()]
)

logger = logging.getLogger()

def create_app():
  logger.info(f"Starting app in {config['FLASK_ENV']}")
  app = Flask(__name__)
  app.config.from_object("config")
  crete_apis(app)
  
  # This shall be removed once metrics is implemented
  @app.route("/_status/healthz")
  def health_ok():
    return "OK"

  return app

if __name__ == "__main__":
  app = create_app()
  app.run(host="0.0.0.0", port=config["FLASK_RUN_PORT"], debug=True)
