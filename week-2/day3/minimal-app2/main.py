from flask import Flask
from markupsafe import escape

app=Flask(__name__)


@app.route("/")
def hello_world():
    al = "<script>alert('hi')</script>"
    return(
        f'''
            Hello, World! Welcome to Flask
            {escape(al)}
        '''
    )
