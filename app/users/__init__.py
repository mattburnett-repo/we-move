from flask import Blueprint, render_template
from app.database.db import get_db

# Create the blueprint for users
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
