from flask import Blueprint, render_template
from app.database.db import get_db

bp = Blueprint('campaigns', __name__)

@bp.route('/', endpoint='campaign_list')
def list_campaigns():
    db = get_db()
    campaigns = db.execute('SELECT * FROM campaigns').fetchall()
    return render_template('campaigns/list.html', campaigns=campaigns)

@bp.route('/<int:campaign_id>', endpoint='campaign_detail')
def get_campaign(campaign_id):
    db = get_db()
    campaign = db.execute('SELECT * FROM campaigns WHERE id = ?', (campaign_id,)).fetchone()
    return render_template('campaigns/detail.html', campaign=campaign)
