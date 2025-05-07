from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database.db import get_db

bp = Blueprint('donations', __name__, url_prefix='/donations')

# List all donations
@bp.route('/', endpoint='donation_list')
def list_donations():
    db = get_db()
    donations = db.execute('''
        SELECT d.*, c.title AS campaign_title
        FROM donations d
        JOIN campaigns c ON d.campaign_id = c.id
        ORDER BY d.donated_at DESC
    ''').fetchall()
    return render_template('donations/list.html', donations=donations)

# Show donation detail
@bp.route('/<int:donation_id>', endpoint='donation_detail')
def donation_detail(donation_id):
    db = get_db()
    donation = db.execute('''
        SELECT d.*, c.title AS campaign_title
        FROM donations d
        JOIN campaigns c ON d.campaign_id = c.id
        WHERE d.id = ?
    ''', (donation_id,)).fetchone()
    return render_template('donations/detail.html', donation=donation)

# Create donation
@bp.route('/create', methods=['GET', 'POST'], endpoint='donation_create')
def create_donation():
    db = get_db()
    users = db.execute('SELECT id, name FROM users').fetchall()
    campaigns = db.execute('SELECT id, title FROM campaigns').fetchall()

    if request.method == 'POST':
        amount = request.form['amount']
        user_id = request.form['user_id']
        campaign_id = request.form['campaign_id']
        db.execute(
            'INSERT INTO donations (amount, campaign_id) VALUES (?, ?)',
            (amount, campaign_id)
        )
        db.commit()
        flash('Donation created successfully.')
        return redirect(url_for('donations.donation_list'))

    return render_template('donations/create.html', users=users, campaigns=campaigns)

# Edit donation
@bp.route('/<int:donation_id>/edit', methods=['GET', 'POST'], endpoint='donation_edit')
def edit_donation(donation_id):
    db = get_db()
    donation = db.execute('SELECT * FROM donations WHERE id = ?', (donation_id,)).fetchone()
    users = db.execute('SELECT id, name FROM users').fetchall()
    campaigns = db.execute('SELECT id, title FROM campaigns').fetchall()

    if request.method == 'POST':
        amount = request.form['amount']
        campaign_id = request.form['campaign_id']
        db.execute(
            'UPDATE donations SET amount = ?, campaign_id = ? WHERE id = ?',
            (amount, campaign_id, donation_id)
        )
        db.commit()
        flash('Donation updated successfully.')
        return redirect(url_for('donations.donation_list'))

    return render_template('donations/edit.html', donation=donation, users=users, campaigns=campaigns)

# Delete donation
@bp.route('/<int:donation_id>/delete', methods=['GET', 'POST'], endpoint='donation_delete')
def delete_donation(donation_id):
    db = get_db()
    donation = db.execute('SELECT * FROM donations WHERE id = ?', (donation_id,)).fetchone()

    if request.method == 'POST':
        db.execute('DELETE FROM donations WHERE id = ?', (donation_id,))
        db.commit()
        flash('Donation deleted successfully.')
        return redirect(url_for('donations.donation_list'))

    return render_template('donations/delete.html', donation=donation)
