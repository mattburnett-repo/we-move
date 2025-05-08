GET_ALL_DONATIONS = """
    SELECT d.*, c.title AS campaign_title, u.name AS donor_name
    FROM donations d
    JOIN campaigns c ON d.campaign_id = c.id
    JOIN users u ON d.donor_id = u.id
    ORDER BY d.donated_at DESC
"""

GET_DONATION_TOTALS_BY_CAMPAIGN = """
    SELECT COUNT(d.amount) AS total_donations, SUM(d.amount) AS total_amount, c.title AS campaign_title
    FROM donations d
    JOIN campaigns c ON d.campaign_id = c.id
    GROUP BY c.id
    ORDER BY total_amount DESC;
"""

# fix user/donor id missing on donations table
# schema and sample data, as well as test data
GET_DONATION_TOTALS_BY_USER = """
    SELECT COUNT(d.amount) AS total_donations, SUM(d.amount) AS total_amount, u.name AS user_name, c.title AS campaign_title
    FROM donations d
    JOIN campaigns c ON d.campaign_id = c.id
    JOIN users u ON d.user_id = u.id
    GROUP BY u.id
    ORDER BY d.donated_at DESC
"""

GET_DONATION_BY_ID = """
    SELECT d.*, c.title AS campaign_title
    FROM donations d
    JOIN campaigns c ON d.campaign_id = c.id
    WHERE d.id = ?
"""

# Needs donor_id 
INSERT_INTO_DONATIONS = """
    INSERT INTO donations (amount, donor_id, campaign_id) VALUES (?, ?, ?)
"""

UPDATE_DONATION_BY_ID = """
    UPDATE donations SET amount = ?, campaign_id = ?, donor_id = ? WHERE id = ?
"""

DELETE_FROM_DONATIONS_BY_ID = """
    DELETE FROM donations WHERE id = ?
"""