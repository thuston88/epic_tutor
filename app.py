# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import os

#os.environ["PA_FLAG"] = "True"

app = Flask(__name__)

@app.route('/')
def homepage():

    title = "Epic Tutorials"

    paragraph = ["Wow, I am learning so much great stuff!  Wow, I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph = paragraph)
    except Exception, e:
        return str(e)
        
@app.route('/index', methods=['GET', 'POST'])
def index():
    notes = [{ "name":"First Note Ever",
        "author":"Tom Huston",
        "content":"This text is coming from the content field"
        },
    { "name":"Finish this Blog",
        "author":"Tom Huston",
        "content":"Show the template control structures"
        },
    { "name":"Deploy this app to pythonanywhere",
        "author":"Tom Huston",
        "content":"When finished coding this app, deploy it to pythonanywhere"
    }]       
    return render_template("mynote.html", notes = notes)
    
@app.route('/env')
def env_vars():
    var_string = []
    for param in os.environ.keys():
        var_list = {param : os.environ[param]}
        var_string.append(var_list)
        
    return render_template("environ.html", var_string = var_string)
    
local_flag = os.getenv("PA_FLAG", "False")        
if __name__ == "__main__":
    app.run()
