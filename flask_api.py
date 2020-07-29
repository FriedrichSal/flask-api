
import os
from io import StringIO
import argparse
import logging
import datetime
import json
from flask import Flask, request, make_response, render_template
from flask_restful import Resource, Api
import pandas as pd
import random

logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)


# Test Resource
class HelloWorld(Resource):
    def get(self):
        logger.info("helle get called")
        return {"hello": "world"}

    def post(self):
        logger.info(request.form)
        # payload as keywords
        # token, team_id, team_domain, channel_id, channel_name, user_id, user_name
        # command, text, response_url, trigger_id
        d = requests.form

        # Retrieve command and text
        command = d["command"]
        text = d["text"]
        print(command)
        print(text)
        assert(command == "/roll")

        # Text should be of the the form xdy+z
        # for rolling a y-sided dice x times and adding z
        # 2d6+3 meansin rolling a six sided dice twice and adding 3 to the sum
        # Might do this with regular expression, but for now just split
        try:
            num_dice = int(text.split("d")[0])
            num_sides = int(text.split("d")[1].split("+")[0])
            split_plus = text.split("d")[1].split("+")
            if len(split_plus) > 1:
                mod = int(split_plus[1])
            else:
                mod = 0
            dice_result = [ random.randint(1,num_sides) for _ in range(num_dice)]
            out = f"Rolling {text}: ({'+ '.join(list(map(str, dice_result)))}) + {mod} = {sum(dice_result) + mod}"
            return out
        except Exception as e:
            print(e)
            return "Something went wrong, try something like: /roll 1d6+2"


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

