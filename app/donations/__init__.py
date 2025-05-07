from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database.db import get_db
from app.database.queries import campaigns, donations, users

bp = Blueprint('donations', __name__, url_prefix='/donations')

# List all donations
@bp.route('/', endpoint='donation_list')
def list_donations():
    db = get_db()
    result = db.execute(donations.GET_ALL_DONATIONS).fetchall()
    return render_template('donations/list.html', donations=result)

# Show donation detail
@bp.route('/<int:donation_id>', endpoint='donation_detail')
def donation_detail(donation_id):
    db = get_db()
    donation = db.execute(donations.GET_DONATION_BY_ID, (donation_id,)).fetchone()
    return render_template('donations/detail.html', donation=donation)

# Create donation
@bp.route('/create', methods=['GET', 'POST'], endpoint='donation_create')
def create_donation():
    db = get_db()
    users_result = db.execute(users.GET_ALL_USERS).fetchall()
    campaigns_result = db.execute(campaigns.GET_ALL_CAMPAIGNS).fetchall()

    if request.method == 'POST':
        amount = request.form['amount']
        # user_id = request.form['user_id']
        campaign_id = request.form['campaign_id']
        db.execute(
            donations.INSERT_INTO_DONATIONS,
            (amount, campaign_id)
        )
        db.commit()
        flash('Donation created successfully.')
        return redirect(url_for('donations.donation_list'))

    return render_template('donations/create.html', users=users_result, campaigns=campaigns_result)

# Edit donation
@bp.route('/<int:donation_id>/edit', methods=['GET', 'POST'], endpoint='donation_edit')
def edit_donation(donation_id):
    db = get_db()
    donation_result = db.execute(donations.GET_DONATION_BY_ID, (donation_id,)).fetchone()
    users_result = db.execute(users.GET_ALL_USERS).fetchall()
    campaigns_result = db.execute(campaigns.GET_ALL_CAMPAIGNS).fetchall()

    if request.method == 'POST':
        amount = request.form['amount']
        campaign_id = request.form['campaign_id']
        db.execute(donations.UPDATE_DONATION_BY_ID,
            (amount, campaign_id, donation_id)
        )
        db.commit()
        flash('Donation updated successfully.')
        return redirect(url_for('donations.donation_list'))

    return render_template('donations/edit.html', donation=donation_result, users=users_result, campaigns=campaigns_result)

# Delete donation
@bp.route('/<int:donation_id>/delete', methods=['GET', 'POST'], endpoint='donation_delete')
def delete_donation(donation_id):
    db = get_db()
    donation_result = db.execute(donations.GET_DONATION_BY_ID, (donation_id,)).fetchone()

    if request.method == 'POST':
        db.execute(donations.DELETE_FROM_DONATIONS_BY_ID, (donation_id,))
        db.commit()
        flash('Donation deleted successfully.')
        return redirect(url_for('donations.donation_list'))

    return render_template('donations/delete.html', donation=donation_result)
