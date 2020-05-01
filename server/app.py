
import os
import connexion
from connexion.resolver import RestyResolver

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api("specs.yml", resolver=RestyResolver('server.api'))
app.add_api("kube_liveness.yml", resolver=RestyResolver(
    'server.api'), options={"swagger_ui": False})
port = os.environ["PORT"] if "PORT" in os.environ else 80
app.run(port=port)
