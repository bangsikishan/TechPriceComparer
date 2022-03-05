from search import Search
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    data_1 = {}
    data_2 = {}

    if request.method == "POST":
        req = request.form

        name = req["tech"]

        if name != "":
            data_1.clear()
            data_2.clear()
            
            obj = Search(name)
            data_1, data_2 = obj.open_url()
        else:
            print("[+] Empty search!")

    return render_template("home.html", site1=data_1, site2=data_2)

if __name__=="__main__":
    app.run(debug=True)