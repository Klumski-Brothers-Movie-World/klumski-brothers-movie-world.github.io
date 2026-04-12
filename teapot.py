from flask import *
app = Flask(__name__) @app.route('/teapot')
def teapot(): 
    return Response("I'm a teapot", status=418)
if __name__ == '__main__': app.run()