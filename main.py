from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/index")
def index():
     return render_template("index.html")
	 
app.route("/index2")
def index2():
     return render_template("1_Speak_recognize.py")

@app.route('/script.php')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    return render_template('index.html', message=forward_message);


if __name__ == "__main__":
    app.run(debug=True)
