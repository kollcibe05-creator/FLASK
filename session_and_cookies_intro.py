from flask import Flask, session, jsonify, make_response, request

app = Flask(__name__)
app.json.compact = False

app.secret_key = b'\x8dI)H\xd65\x85\x9d+\xdb\x18$f\xbb\xcdI'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    session['hello'] = session.get('hello') or 'World'
    session['goodnight'] = session.get("goodnight") or 'Moon'

    response = make_response(
        jsonify({
            'session': {
                "session_key": key, 
                "session_value": session[key], 
                'session_accessed': session.accessed
            }, 
            'cookies': [{cookie: request.cookies[cookie]} for cookie in request.cookies]
        }),
        200
    )

    return response

# Blog Paywall 
@app.route("/articles/<int:id>", methods=['GET'])
def articles(id):
    session['page_view_count'] = session.get('page_view_count', 0) # if 'page_view_count' in session else 0 
    session['page_view_count'] += 1

    if session.get('page_view_count') > 3:
        return make_response({
            'Limit reached': "Maximum Free Tier View Reached."
        }, 
        401
        )
    return Article.query.filter_by(id=id).first().to_dict, 200
    # conditional for not found article


if __name__ == "__main__":
    app.run(port=5555)