from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__) # views é o que é importado no init

@views.route('/')
def home():
    return render_template("index.html")

