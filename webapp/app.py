from flask import Flask, abort

app=Flask(__name__)

@app.route("/")
def success():
    return "it is working"

@app.route("/error")
def error():
    abort(500,"something went wrong")

if __name__=="__main__":
    app.run(debug=True,port=8000,host="0.0.0.0")

#to run locally
#python app.py