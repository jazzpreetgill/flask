from flask import Flask
#WSGI Application
app = Flask(__name__) #initializing the flask application or flask container

@app.route('/') #decorator define URL #https://127.0.0:5000/
#defining function just below decorator mean when user going to vist above URL (defined in the decorator) below function will get trigger
# means decorator bind the URL and function together
def greeting():
    return 'Welcome to Flask this is our first class using Flask'

@app.route('/user') #127.0.0:5000/user
def user():
    return "Welcome Jaspreet"



if __name__=='__main__':
    app.run(debug=True)