from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return '''Here\'s a simple web server using Nginx 
    running in a Docker container. Thanks for visiting!'''
if __name__ == "__main__":
    app.run(host='0.0.0.0')
