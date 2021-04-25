"""
James Taylor's (very simple!) Flask API.
"""

from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

forbidden = ['..', '~', '//']
@app.errorhandler(404)
def not_found_404(e):
    return render_template('404.html')

@app.errorhandler(403)
def forbidden_403(e):
    return render_template('403.html')

@app.route('/<path:fname>')
def get_page(fname):
    if any(i in fname for i in forbidden):
        abort(403)
    return send_from_directory('pages/', fname)

@app.route('/')
def default():
    return send_from_directory('pages/', 'home')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
