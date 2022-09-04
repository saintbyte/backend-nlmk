from __future__ import annotations

import json
import os

import bottle
from bottle import hook
from bottle import response
from bottle import route
from bottle import run
from constants import CORS_ALL_WILDCARD
from constants import CORS_ALLOWED_HTTP_HEADERS
from constants import CORS_ALLOWED_HTTP_METHODS
from constants import JSON_CONTENT_TYPE
from db import db
from helpers import DateTimeEncoder
from models import AtmosphereParameters
from playhouse.shortcuts import model_to_dict

"""
Hook for databases
"""

@hook("before_request")
def _connect_db():
    db.connect(reuse_if_open=True)

@hook("after_request")
def _close_db():
    if not db.is_closed():
        db.close()

@hook("after_request")
def _enable_cors():
    response.headers["Access-Control-Allow-Origin"] = CORS_ALL_WILDCARD
    response.headers["Access-Control-Allow-Methods"] = CORS_ALLOWED_HTTP_METHODS
    response.headers["Access-Control-Allow-Headers"] = CORS_ALLOWED_HTTP_HEADERS


"""
Routes
"""

@route("/atmosphere/parameters/")
def export_vacancy():
    response.content_type = JSON_CONTENT_TYPE
    return json.dumps([model_to_dict(v) for v in AtmosphereParameters.select()], cls=DateTimeEncoder)



@route("/")
def index():
    return "<h1>Its working!</h1>"


app = bottle.default_app()

if __name__ == "__main__":
    run(host="0.0.0.0", port=int(os.environ.get("PORT")))
