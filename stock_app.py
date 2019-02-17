from app import app, db
from app.models import Trades


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Trades": Trades}
