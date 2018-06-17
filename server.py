from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__)
app.secret_key = "ShaneBobMissouri"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if (len(session['name']) or len(session['comment']) > 0) and len(session['comment']) <= 120:
       
        return render_template("results.html", name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])
    
    elif len(session['name']) < 1 or len(session['comment']) < 1:
        flash("Cannot be empty, hoser!")
    
    elif len(session['comment']) > 120:
        flash("Too long, hoser!")
    else:
        return redirect('/')
        

@app.route('/clear', methods=['GET'])
def clear_it():
    session.clear()
    return redirect('/')

app.run(debug=True)