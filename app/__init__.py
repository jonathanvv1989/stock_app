from flask import Flask

app = Flask(__name__)

# At bottom to avoid circular imports in routes.py
from app import routes  # noqa
