GET_ALL_CAMPAIGNS = """
    SELECT c.goal_amount, COUNT(d.amount) AS total_donations, SUM(d.amount) AS total_amount, c.id , c.title, u.name 
    FROM donations d
    RIGHT JOIN campaigns c ON d.campaign_id = c.id
    JOIN users u ON c.user_id = u.id
    GROUP BY c.id
    ORDER BY total_amount DESC;
"""

GET_CAMPAIGN_BY_ID = """
    SELECT c.*, u.name FROM campaigns c 
    JOIN users u ON c.user_id = u.id 
    WHERE c.id = ?
"""

INSERT_INTO_CAMPAIGN = """
    INSERT INTO campaigns (title, description, goal_amount, user_id) 
    VALUES (?, ?, ?, ?)
"""

UPDATE_CAMPAIGN_BY_ID = """
    UPDATE campaigns 
    SET user_id = ?, title = ?, description = ?, goal_amount = ?, is_active = ? 
    WHERE id = ?
"""

DELETE_CAMPAIGN_BY_ID = """
    DELETE FROM campaigns 
    WHERE id = ?
"""