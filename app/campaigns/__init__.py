from flask import Blueprint, request, redirect, url_for, render_template, flash
from app.database.db import get_db

bp = Blueprint('campaigns', __name__)

@bp.route('/', endpoint='campaign_list')
def list_campaigns():
    db = get_db()
    campaigns = db.execute('SELECT c.*, u.name FROM campaigns c JOIN users u ON c.user_id = u.id').fetchall()
    return render_template('campaigns/list.html', campaigns=campaigns)

@bp.route('/<int:campaign_id>', endpoint='campaign_detail')
def get_campaign(campaign_id):
    db = get_db()
    campaign = db.execute('SELECT c.*, u.name FROM campaigns c JOIN users u ON c.user_id = u.id WHERE c.id = ?', (campaign_id,)).fetchone()
    return render_template('campaigns/detail.html', campaign=campaign)

@bp.route('/create', methods=['GET', 'POST'], endpoint='campaign_create')
def create_campaign():
    # Fetch users from the database, for the user dropdown in the create template.
    db = get_db()
    users = db.execute('SELECT id, name FROM users').fetchall()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        goal_amount = request.form['goal_amount']
        user_id = request.form['user_id']

        if not title:
            flash('Title is required.', 'error')
        else:
            db = get_db()
            db.execute(
                'INSERT INTO campaigns (title, description, goal_amount, user_id) VALUES (?, ?, ?, ?)',
                (title, description, goal_amount, user_id)
            )
            db.commit()
            flash('Campaign created successfully!', 'success')
            return redirect(url_for('campaigns.campaign_list'))

    return render_template('campaigns/create.html', users=users)

@bp.route('/<int:campaign_id>/edit', methods=['GET', 'POST'], endpoint='campaign_edit')
def edit_campaign(campaign_id):
    db = get_db()
    if request.method == 'GET':
        campaign = db.execute('''
              SELECT c.*, u.name AS user_name
              FROM campaigns c
              JOIN users u ON c.user_id = u.id
              WHERE c.id = ?
          ''', (campaign_id,)).fetchone()
        users = db.execute('SELECT id, name FROM users').fetchall()
        return render_template('campaigns/edit.html', campaign=campaign, users=users, user_id=campaign['user_id'])
    if request.method == 'POST':
        user_id = request.form['user_id']
        title = request.form['title']
        description = request.form['description']
        goal_amount = request.form['goal_amount']
        is_active = request.form['is_active']
        db.execute('''
                   UPDATE campaigns 
                   SET user_id = ?, title = ?, description = ?, goal_amount = ?, is_active = ? 
                   WHERE id = ?''', 
                   (user_id, title, description, goal_amount, is_active, campaign_id))
        db.commit()
        flash('Campaign updated successfully!', 'success')
        return redirect(url_for('campaigns.campaign_list'))
    return render_template('campaigns/edit.html', campaign=campaign)

@bp.route('/<int:campaign_id>/delete', methods=['POST'], endpoint='campaign_delete')
def delete_campaign(campaign_id):
    db = get_db()
    db.execute('DELETE FROM campaigns WHERE id = ?', (campaign_id,))
    db.commit()
    flash('Campaign deleted successfully!', 'success')

    return redirect(url_for('campaigns.campaign_list'))