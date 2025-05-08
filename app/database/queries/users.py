GET_ALL_USERS = """
    SELECT * FROM users
"""

GET_USER_BY_ID = """
    SELECT u.*, COUNT(d.amount) AS total_donations, SUM(d.amount) AS total_amount
    FROM users u
    LEFT JOIN donations d ON u.id = d.donor_id
    WHERE u.id = ?
    GROUP BY u.id
    ORDER BY total_amount DESC;
"""

GET_ALL_USERS_WITH_CAMPAIGNS_AND_DONATIONS = """
    SELECT u.*, COUNT(d.amount) AS total_donations, SUM(d.amount) AS total_amount
    FROM users u
    LEFT JOIN donations d ON u.id = d.donor_id
    GROUP BY u.id
    ORDER BY total_amount DESC;
"""

INSERT_INTO_USERS = """
    INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)
"""

UPDATE_USER_BY_ID = """
    UPDATE users SET name = ?, email = ?, password_hash = ? WHERE id = ?
"""

UPDATE_USER_BY_ID_NO_PASSWORD = """
    UPDATE users SET name = ?, email = ? WHERE id = ?
"""

DELETE_USER_BY_ID = """
    DELETE FROM users WHERE id = ?
"""