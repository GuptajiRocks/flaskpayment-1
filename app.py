from flask import Flask, render_template, request
from waitress import serve
import mysql.connector as mc
from msq import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def ind():
    return render_template("index.html")

@app.route("/acceptSend")
def send_page():
    return render_template("sendMoney.html")

@app.route("/checkBal")
def all_page():
    data = get_data_from_db()
    return render_template("allBal.html", data=data)

@app.route("/transfer")
def tranfer_money():
    sid = int(request.args.get("userId"))
    rid = int(request.args.get("receiverId"))
    amt = int(request.args.get("amount"))
    
    res = insertMoney(sid, rid, amt)
    if (res == 1):
        return render_template("success.html")
    else:
        return render_template("error.html")

@app.route("/userBalport")
def uidpage():
    return render_template("userBalform.html")

@app.route("/userBaldisp")
def guid():
    sid = request.args.get("userId")
    data = get_transac_by_id(sid)

    if data == 0:
        return render_template("error.html")
    else:
        return render_template("dispid.html", data=data, userIDname=sid)       


if __name__ == "__main__":
    app.run(debug=True)

