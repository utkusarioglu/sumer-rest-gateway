import config
import logging
from flask import Flask
from api import crete_apis

logging.basicConfig(
  level=logging.DEBUG,
  datefmt="%Y-%m-%d %H:%M:%S",
  handlers=[logging.StreamHandler()]
)

logger = logging.getLogger()

def create_app():
  logger.info(f"Starting app in {config.get('APP_ENV')}")
  app = Flask(__name__)
  app.config.from_object("config")
  crete_apis(app)
  
  # This shall be removed once metrics is implemented
  @app.route("/_status/healthz")
  def health_ok():
    return "OK"

  @app.route("/rest/hello")
  def hell_route():
    return {"message": "hello2"}

  return app

if __name__ == "__main__":
  app = create_app()
  app.run(
    host="0.0.0.0", 
    port=config.get("FLASK_RUN_PORT"),
    debug=config.get("DEBUG")
  )
