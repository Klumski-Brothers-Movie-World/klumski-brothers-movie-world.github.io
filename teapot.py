from flask import *
app = Flask(__name__)

@app.route('/teapot')
def teapot():
    html_content = "<h1>I'm a teapot</h1><p>This server is a teapot, not a coffee machine.</p>"
    content = Response(html_content, status=418)
    return content


if __name__ == '__main__':
    app.run()