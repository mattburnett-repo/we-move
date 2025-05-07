GET_ALL_DONATIONS = """
    SELECT d.*, c.title AS campaign_title
    FROM donations d
    JOIN campaigns c ON d.campaign_id = c.id
    ORDER BY d.donated_at DESC
"""

GET_DONATION_BY_ID = """
    SELECT d.*, c.title AS campaign_title
    FROM donations d
    JOIN campaigns c ON d.campaign_id = c.id
    WHERE d.id = ?
"""

INSERT_INTO_DONATIONS = """
    INSERT INTO donations (amount, campaign_id) VALUES (?, ?)
"""

UPDATE_DONATION_BY_ID = """
    UPDATE donations SET amount = ?, campaign_id = ? WHERE id = ?
"""

DELETE_FROM_DONATIONS_BY_ID = """
    DELETE FROM donations WHERE id = ?
"""