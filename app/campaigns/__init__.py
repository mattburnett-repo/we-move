from flask import Blueprint, request, redirect, url_for, render_template, flash
from app.database.db import get_db
from app.database.queries import campaigns, users

bp = Blueprint('campaigns', __name__)

@bp.route('/', endpoint='campaign_list')
def list_campaigns():
    db = get_db()
    results = db.execute(campaigns.GET_ALL_CAMPAIGNS).fetchall()
    return render_template('campaigns/list.html', campaigns=results)

@bp.route('/<int:campaign_id>', endpoint='campaign_detail')
def get_campaign(campaign_id):
    db = get_db()
    results = db.execute(campaigns.GET_CAMPAIGN_BY_ID, (campaign_id,)).fetchone()
    return render_template('campaigns/detail.html', campaign=results)

@bp.route('/create', methods=['GET', 'POST'], endpoint='campaign_create')
def create_campaign():
    # Fetch users from the database, for the user dropdown in the create template.
    db = get_db()
    results = db.execute(users.GET_ALL_USERS).fetchall()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        goal_amount = request.form['goal_amount']
        user_id = request.form['user_id']

        if not title:
            flash('Title is required.', 'error')
        else:
            db = get_db()
            db.execute(campaigns.INSERT_INTO_CAMPAIGN,
                (title, description, goal_amount, user_id)
            )
            db.commit()
            flash('Campaign created successfully!', 'success')
            return redirect(url_for('campaigns.campaign_list'))

    return render_template('campaigns/create.html', users=results)

@bp.route('/<int:campaign_id>/edit', methods=['GET', 'POST'], endpoint='campaign_edit')
def edit_campaign(campaign_id):
    db = get_db()
    if request.method == 'GET':
        campaign_results = db.execute(campaigns.GET_CAMPAIGN_BY_ID, (campaign_id,)).fetchone()
        users_results = db.execute(users.GET_ALL_USERS).fetchall()
        return render_template('campaigns/edit.html', campaign=campaign_results, users=users_results, user_id=campaign_results['user_id'])
    if request.method == 'POST':
        user_id = request.form['user_id']
        title = request.form['title']
        description = request.form['description']
        goal_amount = request.form['goal_amount']
        is_active = request.form['is_active']
        db.execute(campaigns.UPDATE_CAMPAIGN_BY_ID, 
                   (user_id, title, description, goal_amount, is_active, campaign_id))
        db.commit()
        flash('Campaign updated successfully!', 'success')
        return redirect(url_for('campaigns.campaign_list'))
    return render_template('campaigns/edit.html', campaign=campaign_results)

@bp.route('/<int:campaign_id>/delete', methods=['POST'], endpoint='campaign_delete')
def delete_campaign(campaign_id):
    db = get_db()
    db.execute(campaigns.DELETE_CAMPAIGN_BY_ID, (campaign_id,))
    db.commit()
    flash('Campaign deleted successfully!', 'success')

    return redirect(url_for('campaigns.campaign_list'))