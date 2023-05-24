from .. import login_manager
from ..models import Professor

@login_manager.user_loader
def load_prof(prof_id):
    return Professor.query.get(int(prof_id))
