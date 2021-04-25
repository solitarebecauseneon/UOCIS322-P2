"""
James Taylor's (very simple!) Flask API.
"""

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

forbidden = ['..', '~', '//']
@app.errorhandler(404)
def 404_not_found():
    return render_template('404.html')

@app.errorhandler(403)
def 403_forbidden():
    return render_template('403.html')

@app.route('/')
def default():
    return send_from_directory('pages/', 'home')

@app.route('/<path:fname>')
def get_page(fname):
    if any(i in fname for i in forbidden):
        abort(403)
    return send_from_directory('pages/', fname)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
