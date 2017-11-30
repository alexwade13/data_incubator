from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/img/', methods=['POST','GET'])

def imgDisplay():
    print(request.files['picture'],"TESTSTS")
    image = request.files['picture'].read()
    
    return """
    <h1>Hello heroku</h1>
    <body cz-shortcut-listen="true">
        <h1> Automatically deployed! </h1>
        test
        <img src="{image}"/>
    </body>
    

    """


@app.route('/hello')
def hellodd():
    return 'Hello, World'

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    return """
    <h1>Hello heroku</h1>
    <body cz-shortcut-listen="true">
        <h1> Automatically deployed! </h1>
        <form action="/img/" method="post" enctype="multipart/form-data">
            <input type="file" name="picture" accept="image/*">
            <input type="submit">
        </form>
    
    </body>
    <p>It is currently {time}.</p>

    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

