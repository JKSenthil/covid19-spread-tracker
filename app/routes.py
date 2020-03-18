import os
from app import app
from flask import render_template

@app.route('/')
def base():
    data = {"dates":[]}
    lis = os.listdir("./app/data/")
    for file in lis:
        if file[0] == ".":
            continue
        s = file.split("-")
        filename = s[1] + "/" + s[2].split(".")[0] + "/" + "2020"
        data["dates"].append(filename)
    data["l"] = len(lis) - 1
    data["dates"].sort()
    return render_template('base.html', data=data)

@app.route('/data/<date>')
def get_data(date):
    s = ""
    try:
        with open("./app/data/data-" + date + ".txt", "r") as fp:
            line = fp.readline()
            while line:
                s += line
                line = fp.readline()
    except:
        return "exception occurred, either invalid date format or data for requested date does not exist"
    return s