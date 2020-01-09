from flask import Flask
from flask import render_template
from .database import articles
from flask import request
from flask import redirect
from flask import url_for
from flask import session



flask_app = Flask(__name__)
flask_app.secret_key = "b9\x8dC\x07dyg\xcc\x9cx\xefG\x8b\xad\xa6\xe9\xa1\xbd\xcch\xd2\x89"

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def view_about():
    return render_template("about.jinja")

@flask_app.route("/admin/")
def view_admin():
    if "logged" not in session:
        return redirect(url_for("view_login"))
    return render_template("admin.jinja")

@flask_app.route("/articles/")
def view_articles():
    return render_template("articles.jinja", articles=articles.items())

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
    article = articles.get(art_id)
    if article:
        return render_template("article.jinja", article=article)
    return render_template("article_not_found.jinja", art_id=art_id)

@flask_app.route("/login/", methods=["POST"])
def view_login_user():
    username=request.form["username"]
    password=request.form["password"]
    if username=="admin" and password=="admin":
        session["logged"]= True
        return redirect(url_for("view_admin"))
    else:
        return redirect(url_for("view_login"))
@flask_app.route("/login/", methods=["GET"])
def view_login():
    return render_template("login.jinja")

@flask_app.route("/logout/", methods=["POST"])
def logout_user():
    session.pop("logged")
    return redirect(url_for("view_welcome_page"))
