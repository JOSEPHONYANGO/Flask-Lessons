from flask import Flask

app=Flask (__name__)

@app.route("/")

def intro ():
    return"Hello this is my First App"