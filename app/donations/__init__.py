from flask import Blueprint, render_template
from app.database.db import get_db

# Create the blueprint for donations
bp = Blueprint('donations', __name__)

# Route for listing all donations
@bp.route('/', endpoint='donation_list')
def get_donations():
    db = get_db()
    donations = db.execute('SELECT * FROM donations').fetchall()
    return render_template('donations/list.html', donations=donations)

# Route for viewing a single donation detail
@bp.route('/<int:donation_id>', endpoint='donation_detail')
def get_donation(donation_id):
    db = get_db()
    donation = db.execute('SELECT * FROM donations WHERE id = ?', (donation_id,)).fetchone()
    return render_template('donations/detail.html', donation=donation)
