from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database.db import get_db

bp = Blueprint('users', __name__)

# Route for listing all users
@bp.route('/', endpoint='user_list')
def get_users():
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('users/list.html', users=users)

# Route for viewing a single user's detail
@bp.route('/<int:user_id>', endpoint='user_detail')
def get_user(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    return render_template('users/detail.html', user=user)

# Route for creating a new user
@bp.route('/create', methods=['GET', 'POST'], endpoint='user_create')
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password_hash = request.form['password']

        db = get_db()
        db.execute('INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)',
                   (name, email, password_hash))
        db.commit()

        flash('User created successfully.')
        return redirect(url_for('users.user_list'))

    return render_template('users/create.html')

# Route for editing an existing user
@bp.route('/<int:user_id>/edit', methods=['GET', 'POST'], endpoint='user_edit')
def edit_user(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()

    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']

        db.execute('UPDATE users SET name = ?, email = ? WHERE id = ?',
                   (name, email, user_id))
        db.commit()

        flash('User updated successfully.')
        return redirect(url_for('users.user_list'))

    return render_template('users/edit.html', user=user)

# Route for deleting a user
@bp.route('/<int:user_id>/delete', methods=['GET', 'POST'], endpoint='user_delete')
def delete_user(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()

    if request.method == 'POST':
        db.execute('DELETE FROM users WHERE id = ?', (user_id,))
        db.commit()
        flash('User deleted successfully.')
        return redirect(url_for('users.user_list'))

    return render_template('users/delete.html', user=user)
