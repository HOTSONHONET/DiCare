from flask import Flask, render_template, redirect, current_app as app, request, flash
from .Uitls.model import DiCareModel
from config import *

from sqlalchemy import exc
from datetime import datetime
from .database import Patient, db

# Initialzing model
model = DiCareModel()

# Messages
healthy_msg = "Patient is in a good condition..."
unhealthy_msg = "Patient is in a bad condition"

# Setting secret key for app
app.secret_key = SECRET_KEY


# Route for main page
@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html")

# Route for dashboard
@app.route("/dashboard")
def dashboard():
    return redirect("/dashboard/")

# Route for checkNow
@app.route("/checkNow")
def checkNow():
    return render_template("checkNow.html")

# Route for predict
@app.route("/predict", methods = ["POST", "GET"])
def model_predict():
    if (request.method == "GET"):
        return redirect("/")

    name_list = [
        'n_ips',
        'dd_id22',        
        'n_emg_cs',
        'n_ds',
        'n_mds',
        'n_hrhos',
        'n_lps',
        'insln_cnt',
        'age',
        'n_ops',
        'dd_id3',
        'n_ps',
    ]
    data = [int(request.form.get(name)) for name in name_list]
    print(f"Data : {data}")
    prediction = model.predict(data)
    print(prediction)
    

    healthy = False if (prediction['unhealthy'] > prediction['healthy']) else True

    if healthy:
        flash(healthy_msg +"\n" + f"Probabilty : {round(prediction['healthy']*100, 3)}%", "success")
        return redirect("/home")

    flash(unhealthy_msg +"\n" + f"Probabilty : {round(prediction['unhealthy']*100, 3)}%", "danger")
    return render_template("enroll.html")
    

# Route for patient enrollment
@app.route("/enroll", methods = ["POST", "GET"])
def enroll():
    if (request.method == "GET"):
        return redirect("/")

    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    gname = request.form.get('gname')
    cnumber = request.form.get('cnumber')
    desc = request.form.get('desc')
    date = datetime.now()
    
    posts = Patient.query.filter_by().all()
    
    # checking if the patient has been enrolled
    for post in posts:
        if ((post.name == name) and (post.cnumber == cnumber) and (post.gname == gname)):
            flash("Patient is alredy in the database", 'info')
            return redirect("/home")
    
    new_entry = Patient(
        name = name,
        age = age,
        gender = gender,
        cnumber = cnumber,
        desc = desc,
        date = date
    )

    db.session.add(new_entry)
    db.session.commit()

    flash("Patient Successfully enrolled...", "info")
    return redirect("/home")
