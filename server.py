from datetime import datetime
import re
from flask import Flask, request, render_template, redirect
from json import load
import os
from sys import platform
import get_groups

app = Flask(__name__)


@app.route("/")
@app.route("/faculties")
def post_faculties():
    with open("groups.json", encoding='utf-8') as f:
        data = load(f)

    faculties = {}
    for faculty, groups in data.items():
        faculties[faculty] = groups['id']
    for faculty, groups in faculties.items():
        print(faculty)
        print(groups)
    return render_template('faculties.html', faculties=faculties)


@app.route("/faculties/<int:facultyId>")  # Справочник групп
def post_groups(facultyId):
    with open("groups.json", encoding='utf-8') as f:
        data = load(f)
    for faculty, grouplist in data.items():
        print(grouplist['groups'])
        print(facultyId)
        print(grouplist['id'])
        if int(grouplist['id']) == facultyId:
            return render_template('groups.html', groups=grouplist['groups'])

    return redirect(f"/faculties/{facultyId}", 404)


# @app.route("/groups/<int:groupId>/schedule/<int:week>")
# def post_schedule():


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)