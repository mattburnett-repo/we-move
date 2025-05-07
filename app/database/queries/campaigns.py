GET_ALL_CAMPAIGNS = """
    SELECT c.*, u.name FROM campaigns c 
    JOIN users u ON c.user_id = u.id
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