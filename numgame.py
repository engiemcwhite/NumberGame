#pylint:disable=print-statement


from flask import Flask, render_template, request, redirect, session
import random,math
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
@app.route('/')
def index():
    picknum()
    print session['num']
    return render_template("numgame.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/guess', methods=['POST'])
def guess():
    myguess = int(request.form['guess'])
    if(myguess > session["num"]):
        session['guidance'] = "Too high!"
        session['result']="wrong"
    elif(myguess < session["num"]):
        session['guidance'] = "Too low!"
        session['result'] = "wrong"
    else:
        session['guidance'] = str(myguess)+" was the right number!"
        session['result']="right"
    return redirect('/')
    
@app.route('/reset' , methods = ['POST'])
def reset():
    session.pop('guidance')
    session.pop('result')
    session.pop('num')
    return redirect('/')

def picknum():
    if "num" in session:
        return
    else:
        session["num"]=math.ceil(random.randrange(0,99))
        session["result"]="noguess"
    
app.run(debug=True) # run our server