from search import Search
from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, request, flash, redirect, url_for 

app = Flask(__name__)


# SECRET KEY TO PROTECT AGAINST CSRF ATTACKS
app.config["SECRET_KEY"] = "4ff3339c778cd6f741157684b0232071"


# HOME PAGE
@app.route("/", methods=["GET", "POST"])
def home():
    data_1 = {}
    data_2 = {}

    if request.method == "POST":
        req = request.form

        name = req["tech"]

        if name != "":
            data_1.clear()
            data_2.clear()
            
            obj = Search(name.upper())
            data_1, data_2 = obj.open_url()
        else:
            print("[+] Empty search!")

    return render_template("home.html", site1=data_1, site2=data_2)


# REGISTER PAGE
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


# LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"Logged in as {form.email.data}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful! Please check username and password!", "danger")

    return render_template("login.html", title="Login", form=form)




if __name__=="__main__":
    app.run(debug=True)