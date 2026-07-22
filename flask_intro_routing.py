import os
from flask import Flask, request, g, current_app, make_response, redirect, abort

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Welcome to my page!</h1>'
    
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route("/<string:username>") # string, int, float, path
def user(username):
    return f"<h1>Profile for {username}</h1>", 200


# an example of a view function that uses a request body
@app.route("/request/location")
def location():
    host = request.headers.get("Host")
    return f'<h1>The host for this page is {host} and location {g.path}</h1>'

@app.route("/app/app_name")
def app_details():
    appname = current_app.name
    response_body = f"What? A {appname}!!!"

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

@app.route("/redir/redirect")
def redirect():
    return redirect("names.com/collo")

@app.route('/<name>')
def get_name(name):
    match = session.query(Artist).filter(Artist.name == name).first()
    if not match:
        abort(404)
    return f'Your match: {match}'
# To avoid setting up with export FLASK_APP=file.py we use a script
if __name__ == "__main__":
    app.run(port=5555, debug=True)
