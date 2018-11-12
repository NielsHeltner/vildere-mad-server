from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/get-users', methods=['GET'])
def getUsers():
    return "All gut", 200
