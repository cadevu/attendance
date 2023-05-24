from .. import db
def blueprints():
    from .main import main as main_blueprint
    from .aulas_controllers import aulas as aulas_blueprint
    return [main_blueprint,  aulas_blueprint]
