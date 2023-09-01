
m flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = 'a5288a57111b35f98fc47e58a083106476808dd0a206f41c'

@app.route('/hex')
def index():
        flash("Slice Item:")
            return render_template("index.html")
        @app.route('/greet', methods=['POST', 'GET'])
        def greet():
                flash('Hi, this is the Article of the slice ' + str(request.form['name_input']))
                    return render_template("index.html")
