from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database.db import get_db
from app.database.queries import users

bp = Blueprint('users', __name__)

# Route for listing all users
@bp.route('/', endpoint='user_list')
def get_users():
    db = get_db()
    user_results = db.execute(users.GET_ALL_USERS).fetchall()
    return render_template('users/list.html', users=user_results)

# Route for viewing a single user's detail
@bp.route('/<int:user_id>', endpoint='user_detail')
def get_user(user_id):
    db = get_db()
    user_result = db.execute(users.GET_USER_BY_ID, (user_id,)).fetchone()
    return render_template('users/detail.html', user=user_result)

# Route for creating a new user
@bp.route('/create', methods=['GET', 'POST'], endpoint='user_create')
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password_hash = request.form['password']

        db = get_db()
        db.execute(users.INSERT_INTO_USERS,
                   (name, email, password_hash))
        db.commit()

        flash('User created successfully.')
        return redirect(url_for('users.user_list'))

    return render_template('users/create.html')

# Route for editing an existing user
@bp.route('/<int:user_id>/edit', methods=['GET', 'POST'], endpoint='user_edit')
def edit_user(user_id):
    db = get_db()
    user_result = db.execute(users.GET_USER_BY_ID, (user_id,)).fetchone()

    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']

        db.execute(users.UPDATE_USER_BY_ID_NO_PASSWORD,
                   (name, email, user_id))
        db.commit()

        flash('User updated successfully.')
        return redirect(url_for('users.user_list'))

    return render_template('users/edit.html', user=user_result)

# Route for deleting a user
@bp.route('/<int:user_id>/delete', methods=['GET', 'POST'], endpoint='user_delete')
def delete_user(user_id):
    db = get_db()
    user_result = db.execute(users.GET_USER_BY_ID, (user_id,)).fetchone()

    if request.method == 'POST':
        db.execute(users.DELETE_USER_BY_ID, (user_id,))
        db.commit()
        flash('User deleted successfully.')
        return redirect(url_for('users.user_list'))

    # ???
    return render_template('users/delete.html', user=user_result)
