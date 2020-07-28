
import os
from io import StringIO
import argparse
import logging
import datetime
import json
from flask import Flask, request, make_response, render_template
from flask_restful import Resource, Api
import pandas as pd

logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)


# Test Resource
class HelloWorld(Resource):
    def get(self):
        logger.info("helle get called")
        return {"hello": "world"}

    def post(self):
        print("RARARARAR")
        logger.info("helle post called")
        logger.info(request.form)
        # return {"hello": "post world"}
        # import pdb; pdb.set_trace()
        return type(request.form)

# Test query string
class HelloQueryString(Resource):
    def get(self):
        return request.args

    def post(self):
        # import pdb; pdb.set_trace()
        return request.json


# Add Recources
api.add_resource(HelloWorld, "/")
api.add_resource(HelloQueryString, "/qs")


if __name__ == "__main__":
    # Parse arguments on how to start the web app
    parser = argparse.ArgumentParser(description="Parse arguments.")
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        nargs=1,
        default=[80],
        help="port on which to serve the app",
        metavar="PORT",
    )
    parser.add_argument(
        "--dev", action="store_true", help="serve with flask dev server"
    )
    args = parser.parse_args()
    port = args.port[0]
    use_dev_server = args.dev

    # Dev or production server
    # host 0.0.0.0 to allow for outside connections
    logger.info("start dash with flask development server")
    app.run(port=port, debug=True, host="0.0.0.0")

