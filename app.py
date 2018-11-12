from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def getUsers():
    return "All gut", 200

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    #application.debug = True
    app.run()