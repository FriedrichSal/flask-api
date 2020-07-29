# Dice Rolling flask-api for Slackbot backend

This is a simple dice rolling bot, to be used as a backend for a slack bot.

## Getting started locally

Clone the repository and install the dependencies
```
pipenv install
```

Then start the api with

```
pipenv run python flask_api.py -p 8080 
```

You can now roll the dice with curl

```
 curl -d "command=/roll&text=2d6+4" localhost:8080/ 
```

## Deploy as chatbot

For deployment on heroku there is a Procfile in the repository. Refer to Heroku how to deploy.

On slack you need to need to create an app on https://api.slack.com/apps. There add a 'slash command' with name '/roll' and set its request URL to 'https://<yourappname>.herokuapp.com/'. Deploy the slack app to your workspace and that should hopefully be enough.
