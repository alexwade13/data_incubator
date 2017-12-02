from flask import Flask, render_template, request, url_for
from datetime import datetime

import base64
app = Flask(__name__)

@app.route('/img/', methods=['POST','GET'])

def imgDisplay():
    print(request.files['picture'],"TESTSTS")
    print(app.static_url_path)
    image = request.files['picture'].read()
    the_baseSixtyFour = base64.b64encode(image)
    the_t = "test"    
    with open('static/picture_out.png', 'wb') as f:
      f.write(image)

    the_url = url_for('static', filename='picture_out.png')
    print(the_url)
    return """<img style="height:100%"src="{url}"/>""".format(url=the_url)


@app.route('/hello')
def hellodd():
    return 'Hello, World'

@app.route('/')
def homepage():

    return """
    <h1>Hello heroku</h1>
    <body cz-shortcut-listen="true">
        <h1> Automatically deployed! </h1>
        <form action="/img/" method="post" enctype="multipart/form-data">
            <input type="file" name="picture" accept="image/*">
            <input type="submit">
        </form>
    
    </body>

    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

