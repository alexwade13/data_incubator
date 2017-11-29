from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    the_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print (the_time, "penis")
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """

if __name__ == "__main__":
    app.run()