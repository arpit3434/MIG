import os
from flask import Flask, render_template, request, redirect, url_for
from serverless_wsgi import handle_request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', visitor_photos=[])

@app.route('/upload', methods=['POST'])
def upload():

    return redirect(url_for('index'))


def handler(event, context):
    return handle_request(app, event, context)
if __name__ == '__main__':
    app.run(debug=True)