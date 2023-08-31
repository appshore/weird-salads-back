from . import models_generated as models
from open_alchemy import init_yaml
init_yaml("openAPI/schema.yml", models_filename="app/models_generated.py")