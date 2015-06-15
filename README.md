## What is this?

I recently gave a talk at the [Chattanooga-Python-User-Group](http://www.meetup.com/Chattanooga-Python-User-Group/events/222345256/). This repo contains the demo code and slides from the presentation.

It it a demo that shows how you can use webpack to manage your assets with Flask. The following topics are covered:

- How to get a basic Flask app running
- How to get webpack set up
- How to integrate webpack with Flask
- How to configure webpack
- How to use React in a Flask app
- How to set up a kick ass development experience with webpack

## Get set up locally with the demo

You will need both Python and NodeJS installed on your system before continuing.

```
# Set up a working directory and clone the demo app.
mkdir /tmp/demo-flask-webpack && cd /tmp/demo-flask-webbpack
git clone https://github.com/nickjj/demo-for-chattanooga-python-user-group




# Create a virtual environment.
#
# Personally I like virtualenvwrapper:
#   https://virtualenvwrapper.readthedocs.org/en/latest
#
# However you can set up your own environment however you wish.
mkvirtualenv demo-flask-webpack




# Install the demo app's python dependencies.
pip install -r requirements.txt




# Install the demo app's webpack dependencies.
npm install




# Run the webpack dev server.
npm start




# Run the Flask server.
python app.py




# View the page in a browser.
open http://localhost:5000




# (Optionally) build the assets to disk.
npm run-script build
```