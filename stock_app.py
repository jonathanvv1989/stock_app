from app import app, db
from app.models import Trade, Company


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Trade": Trade, "Company": Company}
