from flask import flash, redirect, render_template, request, session
from usuarios_app.models.user import User
from usuarios_app import app
app.secret_key = "estoessecreto"


@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    users = User.getAll()
    print("HOLAAAAA",users)
    return render_template("users.html",all_users=users)

@app.route("/users/new")
def newroute():
    return render_template("new.html",all_users=users)

@app.route("/users/<id>")
def editForm(id):
    data = {
        "id":id
    }
    user=User.getOne(data)
    print("EL USEEEER",user)
    return render_template("edit.html",user=user[0])

@app.route("/users/detail/<id>")
def detail(id):
    data = {
        "id":id
    }
    user=User.getOne(data)
    print("EL USEEEER",user)
    return render_template("detail.html",user=user[0])

@app.route("/users/edit/<id>", methods=["POST"])
def editUser(id):
    print("LLEGUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    data = {
        "id":id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    user=User.edit(data)
    print("EL USEEEER",user)
    return redirect("/")

@app.route("/users/delete/<id>")
def deleteUser(id):
    print("LLEGUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    data = {
        "id":id,
    }
    user=User.delete(data)
    print("EL USEEEER",user)
    return redirect("/")

@app.route('/new', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.new(data)
    return redirect("/")