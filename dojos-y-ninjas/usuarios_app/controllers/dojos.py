from flask import flash, redirect, render_template, request, session
from usuarios_app.models.dojo import Dojo
from usuarios_app.models.ninja import Ninja
from usuarios_app import app
app.secret_key = "estoessecreto"


@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.getAll()
    print("HOLAAAAA",dojos)
    return render_template("dojos.html",dojos=dojos)

@app.route("/dojos/<id>")
def dojosDetail(id):
    data = {
        "id":id
    }
    dojo=Dojo.getOne(data)
    ninjas = Ninja.getNinjas(data)
    print("LOS NINJAAAAS",ninjas)
    return render_template("dojos-ninjas.html",dojo=dojo[0],ninjas=ninjas)

@app.route('/new-dojo', methods=["POST"])
def create_dojo():
    data = {
        "nombre": request.form["nombre"]
    }
    Dojo.new(data)
    return redirect("/")

@app.route('/nuevo-ninja')
def nuevo_ninja():
    dojos = Dojo.getAll()
    return render_template("new-ninja.html",dojos=dojos)

@app.route('/new-ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.new(data)
    print ("DESDE FORMMM:",data)
    return redirect("/")