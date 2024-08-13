from flask import Flask, render_template, redirect, request, session, flash, jsonify
from flask_app import app

from flask_app.models.users import User
from flask_app.models.companies import Company
from flask_app.models.products import Product
from flask_app.models.stars import Star
from flask_app.models.comments import Comment
from flask_app.models.categories import Category

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/register/user', methods=['POST'])
def register_user():
    
    if not User.validate_user(request.form):
        return redirect('/register')
    
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    form = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pass_encrypt
    }

    nuevo_id = User.save(form)
    session['user_id'] = nuevo_id
    return redirect('/dashboard/user')


@app.route('/login/user', methods=['POST'])
def login_user():
    user = User.get_by_email(request.form)
    if not user:
        flash("Email no registrado", "login")
        return redirect("/login")
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Contraseña incorrecta", "login")
        return redirect('/login')
    
    session['user_id'] = user.id
    return redirect('/dashboard/user')


@app.route('/dashboard/user')
def dashboard_user():
    if 'user_id' not in session:
        return redirect('/')
    
    form = {"id": session['user_id']}
    user = User.get_by_id(form)
    
    products = Product.get_by_updated()
    categories = Category.get_all()
    
    return render_template('user/dashboard_user.html', user=user, products=products, categories=categories)


@app.route('/edit/user/<int:id>')
def edit_user(id):
    if 'user_id' not in session:
        return redirect('/')
    
    dicc = {"id": id}
    user = User.get_by_id(dicc)

    return render_template('user/edit_user.html', user=user)


@app.route('/update/user', methods=['POST'])
def update_user():
    if 'user_id' not in session:
        return redirect('/')
    
    User.update(request.form)
    return redirect('/dashboard/user')


@app.route('/logout/user')
def logout_user():
    session.clear()
    return redirect('/')


@app.route('/score', methods=['POST'])
def score():
    if 'user_id' not in session:
        return redirect('/')
    
    Star.save(request.form)
    return redirect('/')


# """Codigo ingresado por Damian"""
@app.route('/comment', methods=['POST'])
def comment():
    if 'user_id' not in session:
        return redirect('/')
    
    Comment.save(request.form)
    return redirect('/')