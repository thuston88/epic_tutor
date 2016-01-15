# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():

    title = "Epic Tutorials"

    paragraph = ["Wow, I am learning so much great stuff!  Wow, I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph = paragraph)
    except Exception, e:
        return str(e)
        
if __name__ == "__main__":
    app.run()
